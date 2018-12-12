package io.radanalytics.eventstreamdecisions;

import java.io.Serializable;

/**
 * Simple POJO bject for event
 */
public class Event implements Serializable
{
    private Integer userId;
    private String eventType;
    private String eventId;
    private String nextEvent;

    /**
     *
     * @return Integer
     */
    public Integer getUserId() {
        return userId;
    }

    /**
     *
     * @return String
     */
    public String getEventType() {
        return eventType;
    }

    /**
     *
     * @return String
     */
    public String getEventId() {
        return eventId;
    }

    /**
     *
     * @return String
     */
    public String getNextEvent() {
        return nextEvent;
    }

    /**
     *
     * @param userId
     */
    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    /**
     *
     * @param eventType
     */
    public void setEventType(String eventType) {
        this.eventType = eventType;
    }

    /**
     *
     * @param eventId
     */
    public void setEventId(String eventId) {
        this.eventId = eventId;
    }

    /**
     *
     * @param nextEvent
     */
    public void setNextEvent(String nextEvent) {
        this.nextEvent = nextEvent;
    }
}

