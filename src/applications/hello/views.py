from django import forms
from django.views.generic import FormView
from django.views.generic import RedirectView


class HelloForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()


class HelloView(FormView):
    form_class = HelloForm
    success_url = "/h/"
    template_name = "hello/hello.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.session.get("name")
        address = self.request.session.get("address")

        context.update(
            {
                "address": address or " ",
                "name": name or "Бродяга",
            }
        )

        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        address = form.cleaned_data["address"]
        self.request.session["name"] = name
        self.request.session["address"] = address
        return super().form_valid(form)


class HelloResetView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.request.session.clear()
        return "/h/"
