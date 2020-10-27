# E-Mail guidelines

An e-mail template in Simplic should follow certain rules to avoid being marked as SPAM. The higher the quality of the content, the more e-mails arrive without problems.

```html
<!DOCTYPE html lang="[language]">
<html>
<head>
    <meta charset="UTF-8">
    <meta name="author" content="[author-name]">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
    <!-- Your mail content -->
</body>
</html>
```

The following attributes should be set in each template

* `lang="[language]"` -> `lang="de"` (select your language)
* `content="[author-name]"` -> `content="Simplic"` (your author name)

If your mail is not `utf-8`, change it so your encoding.

##+ Images

Images sent via `<img />` tag must always have an `alt="<alternative text>"` attribute.

## HTTPS

Links and references should always start with `https://` to ensure an encrypted connection between client and server.
