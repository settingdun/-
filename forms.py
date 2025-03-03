from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField
from wtforms.validators import DataRequired, Length


class MyBaseForm(FlaskForm):
    class Meta:
        locales = ['zh']


class NerForm(MyBaseForm):
    ner_text = TextAreaField('ner_text', validators=[DataRequired(), Length(0, 300)])
    submit = SubmitField('确认')


class EntityForm(MyBaseForm):
    # 请求输入数据作为实体查询的数据
    entity = StringField('entity', validators=[DataRequired()])
    submit = SubmitField('查询')


class RelationForm(MyBaseForm):
    entity1 = StringField('entity1')
    relation = StringField('relation')
    # relation = SelectField('relation', choices=[(1, '无限制')], default=1, coerce=int)
    entity2 = StringField('entity2')
    submit = SubmitField('查询')


class DeleteForm(MyBaseForm):
    entity = StringField('entity', validators=[DataRequired()])
    submit = SubmitField('删除')


class AddForm(MyBaseForm):
    entity = StringField('entity', validators=[DataRequired()])
    submit = SubmitField('增加')


class ChangeForm(MyBaseForm):
    entity1 = StringField('entity1')
    relation = SelectField('relation', choices=[(1, '无限制')], default=1, coerce=int)
    entity2 = StringField('entity2')
    submit = SubmitField('修改')


class ADDRelationForm(MyBaseForm):
    entity1 = StringField('entity1')
    relation = StringField('relation')
    # relation = SelectField('relation', choices=[(1, '无限制')], default=1, coerce=int)
    entity2 = StringField('entity2')
    submit = SubmitField('添加')


class DeleteRelationForm(MyBaseForm):
    entity1 = StringField('entity1')
    relation = StringField('relation')
    # relation = SelectField('relation', choices=[(1, '无限制')], default=1, coerce=int)
    entity2 = StringField('entity2')
    submit = SubmitField('删除')


class ChangeRelationForm(MyBaseForm):
    entity1 = StringField('entity1')
    relation1 = StringField('relation1')
    # relation = SelectField('relation', choices=[(1, '无限制')], default=1, coerce=int)
    entity2 = StringField('entity2')
    submit = SubmitField('添加')
    relation = StringField('relation')


# class QuestionForm(MyBaseForm):
#     entity = StringField('entity', validators=[DataRequired()])
#     submit = SubmitField('问答')

