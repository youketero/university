from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Вариант регистрации на базе класса FormView
from login.forms import MyForm, MyLoginForm, MyPasswordResetConfirm


class MyRegisterFormView(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = MyForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class MyLoginFormView(FormView):
    form_class = MyLoginForm

    success_url = "/"

    template_name = "registration/login.html"

    def form_valid(self, form):
        return super(MyLoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyLoginFormView, self).form_invalid(form)


class MyPasswordResetConfirmView(FormView):

    form_class = MyPasswordResetConfirm

    success_url = "/login"

    template_name = "registration/password_reset_confirm.html"

    def form_valid(self, form):
        return super(MyPasswordResetConfirmView, self).form_valid(form)


    def form_invalid(self, form):
        return super(MyPasswordResetConfirmView, self).form_invalid(form)

