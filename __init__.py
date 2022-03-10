from flask import Flask, render_template, request, redirect, url_for

from db_kark import Db
from post import Post
from oppslagsform import OppslagsForm

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    url_kategori = request.args.get('kategori')

    if url_kategori:
        with Db() as db:
            result = db.getCategory(url_kategori)
        posts = [Post(*x) for x in result]
        return render_template('content.html', posts=posts)
    with Db() as db:
        result = db.getAll()

    posts = [Post(*x) for x in result]
    return render_template('content.html', posts=posts)


@app.route("/post/<int:db_id>")
def single_post(db_id: int):
    with Db() as db:
        result = db.getPost(db_id)
    post = [Post(*x) for x in result]
    return render_template('post.html', posts=post)


@app.route("/nytt_innlegg", methods=["GET", "POST"])
def newPost():
    form = OppslagsForm(request.form)
    if request.method == "POST":
        kategori = form.kategori.data
        brukernavn = form.brukernavn.data
        tittel = form.tittel.data
        Ingress = form.ingress.data
        oppslagstekst = form.oppslagstekst.data
        vals = (kategori, brukernavn, tittel, Ingress, oppslagstekst)
        with Db() as db:
            db.createPost(vals)
        return redirect(url_for("resultat", newPost=True))
    else:
        return render_template('nytt_innlegg.html', form=form)


@app.route("/post/<int:post_id>/rediger", methods=["GET", "POST"])
def rediger(post_id: int):
    if request.method == "POST":
        form = OppslagsForm(request.form)
        kategori = form.kategori.data
        tittel = form.tittel.data
        ingress = form.ingress.data
        oppslagstekst = form.oppslagstekst.data
        db_id = form.id.data
        update_values = (kategori, tittel, ingress, oppslagstekst, db_id)
        with Db() as db:
            db.updatePost(update_values)
        return redirect(url_for("resultat", editPost=True, post_id=post_id))
    else:
        form = OppslagsForm(request.form)
        with Db() as db:
            result = db.getPost(post_id)
        post = [Post(*x) for x in result]

        form.tittel.data = post[0].tittel
        form.ingress.data = post[0].ingress
        form.oppslagstekst.data = post[0].oppslagstekst
        form.id.data = post_id
        return render_template("rediger.html", form=form, post_id=post_id)


@app.route("/post/delete/<int:post_id>")
def delete(post_id):
    if post_id:
        with Db() as db:
            db.deletePost(post_id)
    return redirect(url_for("resultat", deletePost=True))


@app.route("/post/resultat/")
def resultat():
    deletePost = request.args.get('deletePost')
    editPost = request.args.get('editPost')
    newPost = request.args.get('newPost')

    resultat = {'deletePost': deletePost, 'editPost': editPost, 'newPost': newPost}
    return render_template('resultat.html', resultat=resultat)


if __name__ == '__main__':
    app.run(debug=True)
