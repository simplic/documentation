# Requires using the Framework.Core package

```csharp
  using Simplic.Framework.Core;
```

## What is it?
It returns a number/string id based on a selected predefinded scheme in the Simplic application itself.

## How to use it?

```csharp
  SequenceNumberManager.Singleton.Get(">>INSERT NAME OF NUMBERCIRCLE HERE<<").Generate(>>PARAMETERS<<);
```

## Actual example from Simplic.Document:

```csharp
  SequenceNumberManager.Singleton.Get("DocumentManagementBarcode").Generate(document.DocumentDate);
```
