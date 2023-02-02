# Resource Locking

## Description:
The resource locking service allows a user to lock a data set from being altered by other users. This makes it possible to prevent conflicts caused by multiple users simultaneously making changes to the same data set like overwriting changes.

## API:
#### CreateLock
```csharp
    [HttpPost("create-lock")]
    ProducesResponseType(typeof(ResourceLockResult), (int)HttpStatusCode.OK)]
    [ProducesResponseType((int)HttpStatusCode.BadRequest)]
    [ProducesResponseType((int)HttpStatusCode.Unauthorized)]
    public async Task<IActionResult> CreateLock(Guid resourceId)
```
Creates a lock on a resource given by ID if it is not locked yet. A lock automatically expires after 3 minutes if not refreshed.
**Returns:** The resource locked result.

#### RefreshLock
```csharp
    [HttpPut("refresh-lock/{resourceId}")]
    [ProducesResponseType(typeof(ResourceLockRefreshResult), (int)HttpStatusCode.OK)]
    [ProducesResponseType((int)HttpStatusCode.BadRequest)]
    [ProducesResponseType((int)HttpStatusCode.Unauthorized)]
    public async Task<IActionResult> RefreshLock(Guid resourceId)
```
Refreshes a lock on a resource given by ID if the user owns the lock. This resets the time until lock expiration to 3 minutes.
**Returns:** The resource refreshed result.

#### ReleaseLock
```csharp
    [HttpPost("release-lock")]
    [ProducesResponseType(typeof(ResourceLockResult), (int)HttpStatusCode.OK)]
    [ProducesResponseType((int)HttpStatusCode.BadRequest)]
    [ProducesResponseType((int)HttpStatusCode.Unauthorized)]
    public async Task<IActionResult> ReleaseLock(Guid resourceId)
```
Releases a lock on a resource given by ID if the user owns the lock.
**Returns:** The resource locked result.

#### CheckLocked
```csharp
    [HttpGet("{resourceId}")]
    [ProducesResponseType(typeof(ResourceLockResult), (int)HttpStatusCode.OK)]
    [ProducesResponseType((int)HttpStatusCode.BadRequest)]
    [ProducesResponseType((int)HttpStatusCode.Unauthorized)]
    public async Task<IActionResult> CheckLocked(Guid resourceId)
```
Checks if a lock exists on a resource given by ID.
**Returns:** The resource locked result.

## ResourceLockingService:
#### CreateLock
```csharp
    Task CreateLock(Guid resourceId);
```
Creates a lock on a resource given by ID if it is not locked yet. A lock automatically expires after 3 minutes if not refreshed.
**Returns:** The resource locked state.

#### RefreshLock
```csharp
    Task<bool> ReleaseLock(Guid resourceId);
```
Refreshes a lock on a resource given by ID if the user owns the lock. This resets the time until lock expiration to 3 minutes.
**Returns:** The refresh success state.

#### ReleaseLock
```csharp
    Task<bool> RefreshLock(Guid resourceId);
```
Releases a lock on a resource given by ID if the user owns the lock.
**Returns:** The resource locked state.

#### CheckLocked
```csharp
    Task<bool> CheckLocked(Guid resourceId);
```
Checks if a lock exists on a resource given by ID.
**Returns:** The resource locked state.