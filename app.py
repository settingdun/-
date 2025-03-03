from flask import Flask, render_template
from handler import search_entity_handler, search_relation_handler, change_relation_handler
from handler import delete_handler, add_handler, change_handler, delete_relation_handler
from handler import add_relation_handler
from forms import NerForm, EntityForm, RelationForm, DeleteForm, AddForm, ChangeForm
from forms import ADDRelationForm, DeleteRelationForm, ChangeRelationForm
app = Flask(__name__)
app.secret_key = 'secret key'
app.config['WTF_I18N_ENABLED'] = False


@app.route('/')
def Home():
    ner_form = NerForm()
    return render_template('Home.html', form=ner_form)


@app.route('/search_entity', methods=['GET', 'POST'])
def search_entity():
    entity_form = EntityForm()
    res = {'ctx': 'padding', 'entityRelation': ''}
    if entity_form.validate_on_submit():
        res = search_entity_handler.search_entity(entity_form.entity.data)
    return render_template('search_entity.html', form=entity_form, ctx=res['ctx'], entityRelation=res['entityRelation'])


@app.route('/search_relation', methods=['GET', 'POST'])
def search_relation():
    relation_form = RelationForm()
    res = {'ctx': '', 'searchResult': ''}
    if relation_form.validate_on_submit():
        res = search_relation_handler.search_relation(relation_form.entity1.data, relation_form.relation.data, relation_form.entity2.data)
    return render_template('search_relation.html', form=relation_form, ctx=res['ctx'], searchResult=res['searchResult'])



@app.route('/delete', methods=['GET', 'POST'])
def delete():
    delete_form = DeleteForm()
    res = {'ctx': 'padding', 'entityRelation': ''}
    if delete_form.validate_on_submit():
       res = delete_handler.delete(delete_form.entity.data)
    return render_template("delete_entity.html", form=delete_form, ctx=res['ctx'])


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
       add_handler.add(add_form.entity.data)
    return render_template("add_entity.html", form=add_form)


@app.route('/add_relation', methods=['GET', 'POST'])
def add_relation():
    relation_form = ADDRelationForm()
    res = {'ctx': '', 'searchResult': ''}
    if relation_form.validate_on_submit():
        res = add_relation_handler.add_relation(relation_form.entity1.data, relation_form.relation.data, relation_form.entity2.data)

    return render_template('add_relation.html', form=relation_form, ctx=res['ctx'], searchResult=res['searchResult'])


@app.route('/change', methods=['GET', 'POST'])
def change():
    change_form = ChangeForm()
    res = {'ctx': '', 'searchResult': ''}
    if change_form.validate_on_submit():
       res = change_handler.change(change_form.entity1.data, change_form.entity2.data)
    return render_template('change_entity.html', form=change_form, ctx=res['ctx'], searchResult=res['searchResult'])


# 删除关系
@app.route('/delete_relation', methods=['GET', 'POST'])
def delete_relation():
    relation_form = DeleteRelationForm()
    res = {'ctx': '', 'searchResult': ''}
    if relation_form.validate_on_submit():
        res = delete_relation_handler.delete_relation(relation_form.entity1.data, relation_form.relation.data, relation_form.entity2.data)

    return render_template('delete_relation.html', form=relation_form, ctx=res['ctx'], searchResult=res['searchResult'])


# 修改关系
@app.route('/change_relation', methods=['GET', 'POST'])
def change_relation():
    relation_form = ChangeRelationForm()
    res = {'ctx': '', 'searchResult': ''}
    if relation_form.validate_on_submit():
        res = change_relation_handler.change_relation(relation_form.entity1.data, relation_form.relation1.data,
                                                relation_form.entity2.data, relation_form.relation.data)

    return render_template('change_relation.html', form=relation_form, ctx=res['ctx'], searchResult=res['searchResult'])

