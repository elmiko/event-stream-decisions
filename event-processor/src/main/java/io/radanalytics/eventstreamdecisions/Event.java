package io.radanalytics.eventstreamdecisions;

import java.io.Serializable;

/**
 * Simple POJO bject for event
 */
public class Event implements Serializable
{
    private String customerAccountNumber;
    private String customerGeo;
    private String eventId;
    private String eventDate;
    private String eventCategory;
    private String eventValue;
    private String eventSource;
    private String nextEvent = "DEFAULT_NEXT_ACTION";

    /**
     *
     * @return String
     */
    public String getCustomerAccountNumber() {
        return customerAccountNumber;
    }

    /**
     *
     * @return String
     */
    public String getCustomerGeo() {
        return customerGeo;
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
    public String getEventDate() {
        return eventDate;
    }

    /**
     *
     * @return String
     */
    public String getEventCategory() {
        return eventCategory;
    }

    /**
     *
     * @return String
     */
    public String getEventValue() {
        return eventValue;
    }

    /**
     *
     * @return String
     */
    public String getEventSource() {
        return eventSource;
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
     * @param customerAccountNumber
     */
    public void setCustomerAccountNumber(String customerAccountNumber) {
        this.customerAccountNumber = customerAccountNumber;
    }

    /**
     *
     * @param customerGeo
     */
    public void setCustomerGeo(String customerGeo) {
        this.customerGeo = customerGeo;
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
     * @param eventDate
     */
    public void setEventDate(String eventDate) {
        this.eventDate = eventDate;
    }

    /**
     *
     * @param eventCategory
     */
    public void setEventCategory(String eventCategory) {
        this.eventCategory = eventCategory;
    }

    /**
     *
     * @param eventValue
     */
    public void setEventValue(String eventValue) {
        this.eventValue = eventValue;
    }

    /**
     *
     * @param eventSource
     */
    public void setEventSource(String eventSource) {
        this.eventSource = eventSource;
    }

    /**
     *
     * @param nextEvent
     */
    public void setNextEvent(String nextEvent) {
        this.nextEvent = nextEvent;
    }
}

