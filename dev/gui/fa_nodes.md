# Financial accounting nodes

1. Get Fiscal years
> [In] ClientId : Needs the client number from the financial accounting client window. 

> [out] Success : The fiscal years are successful imported to simplic studio.
> [out] Failed : Import failed. See error log.

2. Get genereal ledger accounts
> [In] ClientId : Needs the client number from the financial accounting client window. 
> [In] Financial year : yyyy for the financia year. Insert -1 for the current year.

> [out] Success : The fiscal years are successful imported to simplic studio.
> [out] Failed : Import failed. See error log.

3. Sync business partners
> [In] ClientId : Needs the client number from the financial accounting client window. 
> [In] All : True if all business partners should be compared every time.
> [In] ChangedSince : Compare all who are changed since dd.MM.yyyy .

> If "All" and "ChangedSince" are empty, the timestamp of the last synchronize call is set for "ChangedSince".

> [out] Success : The fiscal years are successful imported to simplic studio.
> [out] Failed : Import failed. See error log.

4. Send accounting sequence
> [In] ClientId : Needs the client number from the financial accounting client window. 
> [In] Commit : Indicates if the seqence of bookings should be commited in the target system.
> [In] Description : Sequence description text.

> [out] Success : The fiscal years are successful imported to simplic studio.
> [out] Failed : Import failed. See error log.