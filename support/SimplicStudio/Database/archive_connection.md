Archive-Connection
===

To use the archiving of documents in the Simplic Studio and Application Server there has to exist a connection in the connection management with the name `SqlArchive`.

The connection must point to a Sybase database that contains an `archive` table.
The archive table must contain the columns `archive_guide` and `archive_blob`.