# Configuration

## Configuration a newsletter

Newsletters can be configurated under the `Contact` menu section.

## FTP-Settings

The newsletter editor enables to updload images that are stored on the local machine. All settings can be found in the `Global Settings` section.

![~/images/newsletter-ftp.png](~/images/newsletter-ftp.png)

The most important part is `FTPPublicUrl`. This url replaces the local file path in the newsletter editor. E.g. the file `C:\images\sample.png` is
configurated in the newsletter editor, it will be replaced with `http://sample.com/sample.png` if `FTPPublicUrl` has the following value: `http://sample.com/`.

The image will be uploaded to the configurated ftp server, and be moved to the `FTPRemoteFolderPath`. E.g. the ftp server is: `sample.com` and `FTPRemoteFolderPath` is `/Newsletter`, images will be updloaded to: `ftp://sample.com/Newsletter`.

## Sending newsletter from grid

To send newsletter from a grid, the grid sql must select the following columns:

* `EMailAddress` - Mail address to send the newsletter to
* `Guid` - Guid from `IT_Contacts`

All other columns are optional and can be used in the newsletter template.

The menu entry to start the send process, must contain the following options:

(Clr/.Net section)

* __Class__: `ApplicationHelper`
* __Namespace__: `Simplic.PlugIn.SAC.UI`
* __Static method__: `SendNewsletter`

## Sending newsletter from script

To send a newsletter using a python script, the `NewsletterHandler` must be used.

```py
from Simplic.PlugIn.SAC.UI import NewsletterHandler

handler = NewsletterHandler(<newsletter>, <newsletter-contact-list>)
handler.Send()
```