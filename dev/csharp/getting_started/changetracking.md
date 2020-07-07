# How to track changes

First you need the simplic change tracking nuget package.
Then choose the poco you want to track. The nuget package contains some attributes

    // Only set it once for each poco because it symbolizes the primary key
    [TrackingKey] 
    
     // This will be responsible for the translation  
    [ChangeTrackingDisplayName(Key ="YourLocalizationKey")]
    
    // Every Property that has this attribute wont be tracked
    [IgnoreChangeTracking]

Assign the attribute **[TrackingKey]** to your primary property that you use to store the poco into the database

Furthermore, every property you want to track and show it with a flexible name (english & german) needs the attribute **[ChangeTrackingDisplayName(Key ="YourTranslationKey")]** 

After that, for every property you dont want to track, assign this attribute to it 
**[IgnoreChangeTracking]**

## Example

    public class Person
    {
        [TrackingKey]
        public Guid Guid { get; set; } = Guid.NewGuid();
        
        [IgnoreChangeTracking]
        public string NameA { get; set; }
        
        [ChangeTrackingDisplayName(Key = "hr_place")]
        public string Place { get; set; }
    }
