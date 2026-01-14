import tkinter as tk
from tkinter import ttk, messagebox
import json
import urllib.request
import urllib.error

# Configuração
URL_BASE = "http://localhost:8080"

# --- Funções de API ---
def api_request(endpoint, dados=None, method='POST'):
    try:
        url = f"{URL_BASE}{endpoint}"
        req = None
        if dados:
            dados_json = json.dumps(dados).encode('utf-8')
            req = urllib.request.Request(url, data=dados_json, method=method)
            req.add_header('Content-Type', 'application/json')
        else:
            req = urllib.request.Request(url, method=method)
            
        with urllib.request.urlopen(req) as response:
            if response.status == 204: return None
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        msg = e.read().decode('utf-8')
        try:
            msg_json = json.loads(msg)
            messagebox.showerror("Erro", msg_json.get('erro', 'Erro desconhecido'))
        except:
            messagebox.showerror("Erro HTTP", f"Código {e.code}")
        return None
    except Exception as e:
        messagebox.showerror("Erro Conexão", str(e))
        return None

# --- Ações da Interface ---
def acao_cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    if not nome or not cpf: return
    
    res = api_request("/clientes", {"nome": nome, "cpf": cpf}, 'POST')
    if res:
        messagebox.showinfo("Sucesso", f"Cliente ID {res.get('id')} Cadastrado!")
        atualizar_lista_clientes()
        entry_nome.delete(0, tk.END)

def acao_reservar():
    cpf = entry_reserva_cpf.get()
    quarto = entry_reserva_quarto.get()
    if not cpf or not quarto: return

    res = api_request("/reservas", {"cpf": cpf, "quarto": int(quarto)}, 'POST')
    if res:
        messagebox.showinfo("Sucesso", f"Reserva {res.get('idReserva')} Confirmada!")
        atualizar_tudo()

def acao_cancelar():
    # Tenta pegar ID da seleção na tabela de RESERVAS primeiro
    selecionado = lista_reservas.selection()
    
    id_para_cancelar = ""
    if selecionado:
        item = lista_reservas.item(selecionado)
        id_para_cancelar = item['values'][0] # ID é a primeira coluna

    # Cria popup já preenchido se tiver selecionado
    top = tk.Toplevel()
    top.title("Cancelar")
    ttk.Label(top, text="Confirmar ID da Reserva:").pack(pady=5)
    
    entry_id_canc = ttk.Entry(top)
    entry_id_canc.pack(pady=5)
    if id_para_cancelar:
        entry_id_canc.insert(0, id_para_cancelar)
    
    def confirmar_cancelamento():
        try:
            val_id = entry_id_canc.get()
            if not val_id: return
            
            id_res = int(val_id)
            res = api_request("/reservas", {"idReserva": id_res}, 'DELETE')
            
            if res and "status" in res:
                messagebox.showinfo("Cancelado", "Reserva cancelada!")
                atualizar_tudo()
                top.destroy()
        except ValueError:
            messagebox.showerror("Erro", "ID inválido")

    ttk.Button(top, text="Confirmar Cancelamento", command=confirmar_cancelamento).pack(pady=10)

def atualizar_lista_clientes():
    lista_clientes.delete(*lista_clientes.get_children())
    clientes = api_request("/clientes", method='GET')
    if clientes:
        for c in clientes:
            lista_clientes.insert("", "end", values=(c['id'], c['nome'], c['cpf']))

def atualizar_tudo():
    # Atualiza Quartos
    lista_quartos.delete(*lista_quartos.get_children())
    quartos = api_request("/quartos", method='GET')
    if quartos:
        for q in quartos:
            status = "Ocupado" if q['ocupado'] else "Livre"
            tipo = "Suíte" if "temJacuzzi" in q else "Simples"
            preco = f"R$ {q['precoPorNoite']}"
            lista_quartos.insert("", "end", values=(q['numero'], tipo, preco, status))
            
    # Atualiza Reservas (NOVO!)
    lista_reservas.delete(*lista_reservas.get_children())
    reservas = api_request("/reservas", method='GET')
    if reservas:
        for r in reservas:
            # Tenta pegar nome do cliente e numero do quarto do objeto aninhado
            nome_cli = r['cliente']['nome'] if 'cliente' in r else "N/A"
            num_quarto = r['quarto']['numero'] if 'quarto' in r else "N/A"
            status_res = r['status']
            lista_reservas.insert("", "end", values=(r['idReserva'], nome_cli, num_quarto, status_res))

# --- Montagem da Tela ---
root = tk.Tk()
root.title("Hotel API Manager v4.0 (Final)")
root.geometry("700x600")

abas = ttk.Notebook(root)
abas.pack(fill='both', expand=True)

# ABA 1: CLIENTES
frame_cad = ttk.Frame(abas)
abas.add(frame_cad, text='Gestão de Clientes')
ttk.Label(frame_cad, text="Novo Cadastro").pack(pady=5)
frm_form = ttk.Frame(frame_cad)
frm_form.pack()
ttk.Label(frm_form, text="Nome:").grid(row=0, column=0)
entry_nome = ttk.Entry(frm_form); entry_nome.grid(row=0, column=1)
ttk.Label(frm_form, text="CPF:").grid(row=0, column=2)
entry_cpf = ttk.Entry(frm_form); entry_cpf.grid(row=0, column=3)
ttk.Button(frm_form, text="Salvar", command=acao_cadastrar).grid(row=0, column=4, padx=5)
ttk.Separator(frame_cad, orient='horizontal').pack(fill='x', pady=10)
ttk.Label(frame_cad, text="Clientes Cadastrados").pack()
cols_cli = ('ID', 'Nome', 'CPF')
lista_clientes = ttk.Treeview(frame_cad, columns=cols_cli, show='headings', height=15)
for col in cols_cli: lista_clientes.heading(col, text=col); lista_clientes.column(col, width=100)
lista_clientes.pack(pady=5)
ttk.Button(frame_cad, text="Atualizar Lista", command=atualizar_lista_clientes).pack()

# ABA 2: RESERVAS
frame_res = ttk.Frame(abas)
abas.add(frame_res, text='Reservas e Quartos')

# Form Reserva
frm_res_form = ttk.Frame(frame_res)
frm_res_form.pack(pady=10)
ttk.Label(frm_res_form, text="CPF:").pack(side='left')
entry_reserva_cpf = ttk.Entry(frm_res_form, width=15); entry_reserva_cpf.pack(side='left', padx=5)
ttk.Label(frm_res_form, text="Quarto:").pack(side='left')
entry_reserva_quarto = ttk.Entry(frm_res_form, width=5); entry_reserva_quarto.pack(side='left', padx=5)
ttk.Button(frm_res_form, text="CRIAR RESERVA", command=acao_reservar).pack(side='left', padx=10)

ttk.Separator(frame_res, orient='horizontal').pack(fill='x', pady=5)

# Tabela Reservas (NOVO)
ttk.Label(frame_res, text="Reservas Ativas").pack()
cols_res = ('ID Reserva', 'Cliente', 'Quarto', 'Status')
lista_reservas = ttk.Treeview(frame_res, columns=cols_res, show='headings', height=6)
for col in cols_res: lista_reservas.heading(col, text=col); lista_reservas.column(col, width=100)
lista_reservas.pack()

# Botão Cancelar Inteligente
ttk.Button(frame_res, text="Cancelar Reserva Selecionada", command=acao_cancelar).pack(pady=5)

ttk.Separator(frame_res, orient='horizontal').pack(fill='x', pady=10)

# Tabela Quartos
ttk.Label(frame_res, text="Status dos Quartos").pack()
cols_q = ('Quarto', 'Tipo', 'Preço', 'Status')
lista_quartos = ttk.Treeview(frame_res, columns=cols_q, show='headings', height=6)
for col in cols_q: lista_quartos.heading(col, text=col); lista_quartos.column(col, width=80)
lista_quartos.pack()

ttk.Button(frame_res, text="Atualizar Todas as Tabelas", command=atualizar_tudo).pack(pady=10)

root.mainloop()