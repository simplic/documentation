# Opt-in and Opt-out

The simplic newsletter supports opt-in and opt-out. To do this, the following links must be placed in the newsletter:

`http://newsletter.simplic.biz/?LicenseId={LicenseId}&NewsletterId={NewsletterId}&CustomerId={CustomerId}&language=de-DE`.

The `&language` parameter is optional and can be removed. The default value is `de-De`.

## Design

For showing the newsletter opt-in and opt-out pages, three html templates must be designed. The pages can only be registered by the simplic support
or development team.

### Index.cshtml

```html
@{
    ViewBag.Title = "Newsletter";
}

<center>
    <p>
        <img src="~/Content/Custom/@ViewBag.LicenseId/logo.jpg" />
    </p>

    <p>
        Would you like to receive newsletter from us ?
    </p>

    <p>
        @using (Html.BeginForm("SubmitDecision", "Home", FormMethod.Post, new { id = "frm" }))
        {
            <input type="hidden" name="licenseId" value="@ViewBag.LicenseId" />
            <input type="hidden" name="newsletterId" value="@ViewBag.NewsletterId" />
            <input type="hidden" name="customerId" value="@ViewBag.CustomerId" />
            <input type="hidden" name="language" value="@ViewBag.Language" />
            <input type="hidden" id="chk_sub" name="subscribe" />

<p>
        <input type="button" value="Yes, I would like to receive newsletters" onclick="sendForm('ok')" />

        @if (Request.QueryString["HideUnsubscribe"] == "yes")
        {
            // dont show unsubscribe button
        }
        else
        {
            <input type="button" value="No, I don't want to." onclick="sendForm('cancel')" />
        }
    </p>

        }
    </p>

</center>

<script>
    function sendForm(decision) {
        document.getElementById("chk_sub").value = decision;
        document.getElementById("frm").submit();
    }
</script>
```

### Subscribed.cshtml

```html
@{
    ViewBag.Title = "Newsletter";
}

<center>
    <p>
        <img src="~/Content/Custom/@ViewBag.LicenseId/logo.jpg" />
    </p>

    <p>
        You have <b>subscribed</b> to our newsletter successfully!        
    </p>
</center>
```

### Unsubscribed.cshtml

```html
@{
    ViewBag.Title = "Newsletter";
}

<center>
    <p>
        <img src="~/Content/Custom/@ViewBag.LicenseId/logo.jpg" />
    </p>

    <p>
        You are <b>unsubscribed</b> from our newsletter list!        
    </p>
</center>
```