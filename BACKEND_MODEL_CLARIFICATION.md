# Backend Model Clarification: Talks vs Sessions

## Current State Analysis

After analyzing the SpeakWise backend, there are **two similar models** that can cause confusion:

### 1. Sessions Model (Primary - Currently Used)
**Location**: `/speakwise/events/models.py`
**Status**: ✅ **ACTIVE AND RECOMMENDED**

```python
class Session(TimestampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="sessions")
    speaker = models.ForeignKey(SpeakerProfile, on_delete=models.SET_NULL, null=True, blank=True)
```

**Key Features**:
- Connected to Event model via ForeignKey
- Connected to SpeakerProfile via ForeignKey (one speaker per session)
- Used by frontend via `/api/events/{id}/sessions/` endpoint
- Has proper serializers with speaker details
- Active API endpoints for CRUD operations

### 2. Talks Model (Legacy - Not Currently Used)
**Location**: `/speakwise/talks/models.py`
**Status**: ⚠️ **LEGACY/ALTERNATIVE IMPLEMENTATION**

```python
class Talk(TimestampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="talks")
    speakers = models.ManyToManyField(SpeakerProfile, related_name="talks")
    # Other fields...
```

**Key Features**:
- Connected to Event model via ForeignKey
- Connected to SpeakerProfile via ManyToMany (multiple speakers per talk)
- Has API endpoints at `/api/talks/`
- **NOT currently used by the frontend**

## Current Frontend Implementation

The frontend is correctly using the **Sessions model**:

```typescript
// Frontend API call
GET /api/events/{eventId}/sessions/

// Response includes speaker_details via SessionSerializer
{
  "id": 1,
  "name": "Session Name",
  "speaker_details": {
    "id": 1,
    "full_name": "Speaker Name",
    "avatar": "/media/speakers/avatars/image.jpg",
    "organization": "Company"
  }
}
```

## Recommendations

### ✅ Keep Using Sessions Model
**Reasons**:
1. Already integrated with frontend
2. Proper relationship structure (Event -> Session -> Speaker)
3. Active API endpoints with proper serialization
4. Fits the current application workflow

### 🔄 Consider Talks Model for Future Features
**If you need**:
- Multiple speakers per presentation
- More complex talk management
- Different event structure

### 🧹 Optional Cleanup Actions

1. **Document the Purpose**: Add clear docstrings to both models explaining their intended use
2. **Consider Renaming**: If both models will coexist, rename them for clarity:
   - `Session` → `EventSession` 
   - `Talk` → `MultiSpeakerTalk`
3. **Archive Unused Code**: If Talks model won't be used, consider moving it to a separate file or archiving

## Fixed Issues

### ✅ Speaker Image Display
- **Problem**: Speaker avatars not displaying in EventSessions component
- **Solution**: Added proper URL construction for avatar images
- **Location**: `/components/events/event-sessions.tsx`

**Changes Made**:
```typescript
// Added API_BASE_URL constant
const API_BASE_URL = 'http://127.0.0.1:8000';

// Added helper function for avatar URLs
const getAvatarUrl = (avatarPath: string | undefined) => {
    if (!avatarPath) return null;
    if (avatarPath.startsWith('http://') || avatarPath.startsWith('https://')) {
        return avatarPath;
    }
    return `${API_BASE_URL}${avatarPath.startsWith('/') ? '' : '/'}${avatarPath}`;
};

// Updated avatar rendering with error handling
{session.speaker_details.avatar && getAvatarUrl(session.speaker_details.avatar) && (
    <AvatarImage
        src={getAvatarUrl(session.speaker_details.avatar)!}
        alt={session.speaker_details.full_name}
        onError={(e) => {
            e.currentTarget.style.display = 'none';
        }}
    />
)}
```

### ✅ Model Relationship Clarification
- **Sessions Model**: One-to-One speaker relationship (current implementation)
- **Talks Model**: Many-to-Many speaker relationship (alternative)
- **Frontend**: Uses Sessions model correctly

## Next Steps

1. **Test the Image Fix**: Verify speaker avatars display correctly in the event sessions
2. **Decide on Model Strategy**: Choose whether to keep both models or consolidate
3. **Update Documentation**: Add clear comments in the model files about their purposes
4. **Consider API Consistency**: Ensure all frontend components use the Sessions API consistently

## API Endpoints Currently Used

### ✅ Active (Sessions)
- `GET /api/events/{id}/sessions/` - List event sessions
- `POST /api/events/{id}/sessions/create/` - Create session with speaker
- `PUT /api/events/sessions/{id}/` - Update session
- `DELETE /api/events/sessions/{id}/` - Delete session

### ⚠️ Alternative (Talks)
- `GET /api/talks/` - List talks
- `POST /api/talks/` - Create talk
- `PUT /api/talks/{id}/` - Update talk
- `DELETE /api/talks/{id}/` - Delete talk

The frontend should continue using the Sessions endpoints for consistency.
