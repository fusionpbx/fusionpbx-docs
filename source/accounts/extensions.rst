.. Title:: Extensions

************
Extensions
************

**Extensions** define the necessary information for an endpoint, such as a hard phone, soft phone, or other devices, to 
connect to the SIP server. The extension serves as the SIP username, and the password is the secret used for 
authentication. The domain name system (DNS) locates the server to register with and determines the realm, which 
specifies the domain the endpoint is registering to.

************************************************
Basic Settings
************************************************

Overview
++++++++++++
* **Extension**

   Accepts alphanumeric values for the extension. The default configuration allows for 2–7 digit extensions. Alphanumeric 
   extensions combine letters and numbers, providing flexibility for various use cases. They can help identify departments 
   or roles, such as SALES1 or SUPPORT2, and personalize extensions for employees, like JOHN1 or SARAH2.

* **Range**

   This option is only visible when creating an extension and allows for you to create a block of extensions at once. 
   Enter the number of extensions to create, with each subsequent extension incrementing by 1.

* **Voicemail Password**

   Enter the numeric voicemail password here.

* **Account Code**

   Used with billing systems. If you don’t have a billing system, this field is optional.

* **Effective Caller ID Name**

   The internal caller ID name that will be displayed on other internal phones when receiving a call from this extention. 

* **Effective Caller ID Number**

   The internal caller ID number, typically set to the extension number. This number will be displayed on other internal 
   phones when receiving a call from this extension.

* **Outbound Caller ID Name**

   Used by the outbound route for the external caller ID name. Typically, the business or organization name is set here. 
   Note that your SIP provider may or may not allow this name to be transmitted to the receiving party.

* **Outbound Caller ID Number**

   Used by the outbound route for external caller ID number. Typically, the business or organization number is set here.

*  **Emergency Caller ID Name**

    This is used when calling emergency services, like 911.

*  **Emergency Caller ID Number**

    This is used when calling emergency services, like 911.

* **Directory Full Name**

    The first and last name used to populate the directory. You can access the directory by dialing *411.

* **Directory Visible**

    This setting determines whether the extension number will be hidden or visable to the directory. 

* **Directory Extension Visible**

    This setting determines whether the extension number will be announced to the caller when searching for a user 
    in the directory.

* **Max registrations**
    
    Set the maxium number of registrations for this user. 

* **Limit Max**

    Set the maximum number of outgoing calls for this user.

* **Limit Destination**

    Set the destination for calls when the maximum number of outgoing calls have been reached. The default setting 
    is :code:`!USER_BUSY`. 

*  **Voicemail Enabled** 
   	
    Enable or disable voicemail for this extension.

*  **Voicemail Mail To** 	

    The email address for sending voicemail notifications. Multiple email addresses can be entered, separated by commas. 

*  **Voicemail File** 	

    Select whether to send the voicemail as an attachment (wav file) or as a link in the email. 

*  **Voicemail Keep Local** 	

    Choose whether to keep the voicemail in the system after sending the email notification. 
    Selecting "false" will delete the voicemail after it is sent.

*  **Missed Call**

    This option sends an email for each missed call. To enable this option, you must enter an email address.

*  **Toll Allow** 	

    Enter the toll allow value here. (Examples: domestic,international,local) For example, if you set Toll Allow 
    to "domestic," the extension will only be allowed to make domestic calls, while calls to international or other 
    restricted destinations would be blocked. You can create custom values such as "domestic," "international," 
    or "local" depending on the dialing restrictions or rate plans you want to enforce for that extension.

*  **Call Timeout** 	

    This setting defines the amount of time the system will wait while an extension rings before considering 
    the call to be unanswered. This timeout is typically used to determine how long the system will attempt to 
    connect a call to an extension before it moves on to the next step in the dial plan, such as going to voicemail 
    or routing the call elsewhere.

*  **Call Group** 	

    When a call is routed to a call group, it will be directed to all extensions within that group. This can be 
    useful for handling calls that need to be answered by multiple people within the same department. For example, 
    if you route calls to the "sales" group, all extensions assigned to the "sales" call group will ring when a call 
    is directed to that group.

*  **Call Screen** 	

     enables a feature where the system prompts the caller to identify themselves before the call is connected to 
     the recipient. When this option is enabled, the caller is asked to state their name or provide an identifying 
     message, which is then recorded. The recorded response is presented to the person receiving the call, allowing 
     them to decide whether to accept or reject the call based on the caller's identity. This feature can be 
     particularly useful for businesses that want to screen calls and avoid unwanted or unknown callers.

*  **Record** 	

    The Record setting determines whether calls made to or from a specific extension should be 
    recorded. You can configure it to record:

    * Local calls: Calls made internally between extensions.
    * Inbound calls: Calls received from external sources.
    * Outbound calls: Calls placed to external destinations.
    * All calls: A setting that records every call, regardless of whether it's inbound, outbound, or local.
  
    This feature is useful for tracking, monitoring, or maintaining records of conversations for compliance, 
    quality assurance, or other purposes. The recording typically results in audio files stored in the system, 
    which can be accessed or managed as needed.

*  **Hold Music** 	

    This setting allows you to select the music or ringtone that will be played to callers who are placed on 
    hold by this extension. This feature helps enhance the caller experience by providing audio while they wait, 
    preventing silence and creating a more professional impression.

    You can choose from a variety of pre-uploaded music tracks or ring tones, or you may upload custom audio 
    files to be used as hold music. This music plays during call hold periods until the call is resumed by the 
    extension user or transferred to another destination.

   **Language**

    The Language setting allows you to select the preferred language, voice, and dialect for 
    the extension. This setting impacts various aspects of the system, such as voicemail prompts, 
    IVR (Interactive Voice Response) menus, and other voice-related features.
   
   **Type**

    This setting determines the registration method for an extension or device.

    * Default: This option enables registration for the extension, meaning it allows the 
      device (e.g., hard phone, soft phone) to register with the SIP server, making it active and able to 
      send/receive calls.

    * Virtual: This option disables registration and creates a virtual extension, which does not require 
      a physical device to register. This can be useful for extensions that don’t need to be tied to a specific 
      device, such as for voicemail, call forwarding, or other non-registered use cases.

    In summary, Default is used for regular extensions that need SIP registration, while Virtual is used for 
    extensions that don’t require direct device registration but may still perform other functions.

    **Domain**

    * This setting refers to the domain name or IP address associated with the SIP server or PBX system. This 
      setting is used to identify and route calls for a particular domain within the system.

    When you select a domain, it determines which domain the extension or device is registering with, and 
    it is crucial for routing calls within multi-domain environments.

*  **Context** 	

    * The Context setting in FusionPBX defines the logical grouping or scope of call processing for a specific 
      extension or device. It determines which set of rules or configurations should be applied to the calls 
      coming from or going to that extension.

    By default, the Context is set to match the domain name or IP address of the system. This means that 
    calls associated with that domain or IP will use the default set of rules defined for that domain context.

*  **Enabled**

    * This setting determines whether a specific extension is active or inactive. 
      When set to Enabled, the extension is active and can make or receive calls, register with the SIP server, and 
      function normally within the system.  When set to Disabled, the extension is inactive. It will not be able to 
      make or receive calls, and it will not register with the SIP server. This is useful when temporarily deactivating 
      an extension without deleting it from the system.

     This setting allows administrators to quickly disable an extension without losing its configuration, which 
     can be useful for maintenance, testing, or temporarily removing access for a user.

*  **Description**

    This setting allows you to add a custom label or note to an extension. This is typically used 
    for identifying the extension's purpose or the person associated with it.

    For example, you might use this field to provide details such as:

    * The name of the person using the extension (e.g., "John Doe's Desk Phone").
    * The department or role the extension serves (e.g., "Sales Team Extension").
    * Special instructions or notes about the extension.
   
    The Description is helpful for administrators to manage and quickly identify extensions, especially in larger systems 
    with many extensions. It does not affect the functionality of the extension itself; it’s purely for organizational purposes.



Advanced Settings
==================

.. warning::

   Exercise caution when modifying advanced settings within extensions. Ensure you fully understand the purpose and impact of any changes, as incorrect configurations can disrupt the extension's functionality. Always back up your settings before making adjustments.

Advanced
==========

    **Auth ACL**
    
    This setting is used to define an Access Control List (ACL) for authentication. This ACL is a set of rules that control which IP addresses or subnets are allowed to register or authenticate with the system. It helps enhance security by limiting access to the FusionPBX system based on specific network criteria.

    **CIDR**
    
    The CIDR (Classless Inter-Domain Routing) setting in FusionPBX is used to specify IP address ranges in a compact, efficient 
    format. CIDR notation is commonly used to define network subnets and control access to the system based on IP ranges.

    In simpler terms, CIDR allows you to define a range of IP addresses by combining an IP address with a subnet mask. For 
    example, a CIDR block like 192.168.1.0/24 refers to all IP addresses from 192.168.1.0 to 192.168.1.255.

    When configured in FusionPBX, this setting can be used to define which IP ranges (e.g., subnets or individual addresses) are allowed to connect 
    to the system or specific features.  Network Segmentation: You can use CIDR to manage different parts of your network 
    and apply different rules for different segments.  For example, if you want to restrict access to your FusionPBX server to only certain subnets, you would specify those IP ranges in CIDR notation under this setting.

    The CIDR setting is typically used by advanced users or network administrators who need to configure more precise network 
    security or routing rules.

    **SIP Force Contact**
    
    The SIP Force Contact setting in FusionPBX controls how the SIP contact header (which includes the IP address and port) is 
    handled when the SIP message is processed. This is particularly useful in environments with Network Address Translation (NAT) 
    or other network configurations that require specific handling of contact information.

    The options are as follows:

    * Rewrite Contact IP and Port: This option rewrites both the IP address and the port in the SIP contact header. It's 
    typically used when you want to force the system to always use a specific IP address and port combination for communication, 
    regardless of the original contact information in the SIP message. This setting is useful in cases where SIP devices behind 
    NAT or firewalls need a fixed contact IP and port for consistent communication.

    * Rewrite Contact IP and Port 2.0: This may be a variation or update to the first option, specifically for newer configurations 
    or additional handling of contact headers. It's likely designed for improved SIP communication in more complex network 
    environments or to handle newer versions of SIP-related standards or devices.

    * Rewrite TLS Contact Port: This option specifically targets SIP communication over TLS (Transport Layer Security). TLS is 
    used for encrypted SIP communication, and this setting allows you to control the port used for TLS-secured SIP connections. 
    This can be important in environments where SIP over TLS is required for security reasons, and the contact port needs to 
    be explicitly defined.

    In summary, the SIP Force Contact setting allows you to control how contact information is rewritten for SIP 
    communication, providing flexibility in handling SIP devices, especially when dealing with network configurations that 
    require precise management of IP addresses and ports.

    **SIP Force Expires**

    This setting is used to control the expiration time for SIP registrations and to prevent stale or 
    outdated registrations from being maintained.

    SIP Force Expires allows the server to override the expiration time that the client (SIP device or endpoint) has set 
    for its registration. This ensures that the registration is refreshed more frequently, even if the client has specified 
    a longer expiration time.

    The main purpose of this setting is to ensure that SIP registrations do not become stale. If a SIP device does not refresh 
    its registration within the expected time frame, it could lead to missed calls or communication issues. By setting SIP Force 
    Expires, the server can enforce a stricter refresh rate, preventing any stale registrations from persisting.

    In practice, this setting is particularly useful in dynamic environments where SIP clients may be behind 
    NAT (Network Address Translation), or in cases where SIP devices may not always adhere to optimal registration refresh 
    intervals. By forcing a specific expiration time, FusionPBX can ensure that SIP registrations are kept up-to-date, maintaining 
    better communication reliability and preventing potential connectivity issues.

    **MWI Account**

    This setting is used to specify the Message Waiting Indicator (MWI) account that will monitor the 
    voicemail box for a particular extension.

    MWI (Message Waiting Indicator) is a feature used in SIP systems to indicate whether there are unread voicemail messages. 
    This is typically represented by a blinking light or a visual indicator on the phone or device, signaling that the user has 
    new voicemail.

    The MWI Account setting allows you to define the specific voicemail account that will be monitored for message waiting 
    notifications. The value entered in this setting follows the format user@domain, where:

    * user is the voicemail box (or extension) to be monitored.
    * domain is the domain associated with the system, often matching the SIP server's domain or the PBX domain.

    For example, if the extension 1001 has voicemail, and the domain of your system is example.com, you might set the MWI 
    Account to 1001@example.com.

    **SIP Bypass Media**

    This setting determines how the media stream (audio or video) is handled during a call.

    * Bypass Media: If enabled, the media stream (RTP packets) is sent directly between the 
      endpoints (e.g., phones or devices), bypassing the PBX. This reduces the load on the PBX server and can improve 
      performance by minimizing latency, especially in systems with high call volumes.

    * Proxy Media: If bypass media is not enabled, the PBX acts as a proxy for the media stream. This means the media 
      flows through the PBX server, allowing features like call recording, transcoding, or NAT traversal to be applied. 
      This mode is necessary for certain advanced functionalities but increases the server's resource usage.

    **Absolute Codec String**

    This setting allows you to specify a fixed list of audio codecs for the extension.

    When this setting is configured, the PBX will enforce the use of only the codecs listed in the string for calls involving 
    this extension. This can be useful in scenarios where specific codecs are required for compatibility, performance 
    optimization, or integration with external systems.

    For example:

    If your network requires low-bandwidth codecs, you might specify G729 or G723.
    For higher-quality audio, you might specify PCMU, PCMA, or G722.
    The format of the string should list the codecs in order of priority, separated by commas (e.g., G722,PCMU,PCMA).

    **Force ping**

    This setting determines whether the PBX will send SIP OPTIONS messages to an extension to verify its reachability.

    When enabled, the PBX periodically sends these messages to the extension to confirm that it is still registered and 
    responsive. This can help detect and handle situations where an extension becomes unreachable due to network issues or 
    other disruptions.

    This setting is particularly useful in environments where maintaining real-time awareness of endpoint status is critical, 
    such as call centers or systems with high availability requirements. If disabled, the PBX will not actively check the 
    extension's status using SIP OPTIONS messages.

    **Dial String**

    This setting defines the SIP URI or path used to locate the endpoint for this extension.

    This value specifies how the PBX should contact the extension during a call. It typically includes information like the 
    protocol (e.g., SIP), the username, and the domain or IP address of the endpoint.

    For example, it might look like sofia/internal/1001@domain.com, indicating the protocol, the extension (1001), and 
    the domain to which the PBX will route the call.

    This setting is automatically generated in most cases and usually doesn’t require manual modification unless there is a 
    specific need for custom routing or advanced configurations.
