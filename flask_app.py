import os
from flask import Flask, redirect, render_template, request, url_for, flash
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

app = Flask(__name__)
# O Flash message do Flask exige uma chave secreta
app.config["SECRET_KEY"] = "chave_secreta_para_validacao"
app.config["DEBUG"] = True

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)


# 1. READ (Ler todos os pedidos de passeio)
@app.route("/", methods=["GET"])
def index():
    # Busca os pedidos ordenados pelo mais recente
    response = supabase.table("orders").select("*").order("created_at", desc=True).execute()

    orders = response.data
    return render_template("index.html", orders=orders)


# 2. CREATE (Criar nova solicitação de passeio)
@app.route("/solicitar", methods=["POST"])
def solicitar():
    dog_name = request.form.get("dog_name")
    duration = request.form.get("duration")
    address = request.form.get("address")

    # Validação básica de dados (Requisito obrigatório)
    if not dog_name or not duration or not address:
        flash("Todos os campos são obrigatórios!", "danger")
        return redirect(url_for("index"))

    # Insere no Supabase
    supabase.table("orders").insert({
        "dog_name": dog_name,
        "duration": int(duration),
        "address": address,
        "status": "Pendente"
    }).execute()

    flash("Solicitação de passeio enviada com sucesso!", "success")
    return redirect(url_for("index"))


# 3. UPDATE (Atualizar status ou dados do passeio)
@app.route("/editar/<int:order_id>", methods=["GET", "POST"])
def editar(order_id):
    if request.method == "POST":
        novo_status = request.form.get("status")
        novo_endereco = request.form.get("address")

        # Atualiza no Supabase
        supabase.table("orders").update({
            "status": novo_status,
            "address": novo_endereco
        }).eq("id", order_id).execute()

        flash("Pedido atualizado com sucesso!", "success")
        return redirect(url_for("index"))

    # GET: Busca o pedido específico para exibir na tela de edição
    response = supabase.table("orders").select("*").eq("id", order_id).execute()
    order = response.data[0] if response.data else None
    return render_template("edit_order.html", order=order)


# 4. DELETE (Cancelar/Excluir solicitação)
@app.route("/deletar/<int:order_id>", methods=["POST"])
def deletar(order_id):
    supabase.table("orders").delete().eq("id", order_id).execute()
    flash("Solicitação cancelada com sucesso!", "warning")
    return redirect(url_for("index"))
