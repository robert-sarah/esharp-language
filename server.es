SECURE
    ALLOCATE MEMORY FOR EXECUTION END
    
    TRANSMIT "--- E# ROBUST SERVER STARTING ---" TO CONSOLE END
    
    ESTABLISH INTEGER PORT_NUMBER AS 8080 END
    ESTABLISH RESISTANT STRING SERVER_NAME AS "E-Sharp Hyper Server" END
    ESTABLISH STRING WELCOME_MSG AS "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nWelcome to the E# Hyper Server! Resistance is futile." END
    
    INITIALIZE SERVER ON PORT PORT_NUMBER END
    
    # Listen for a single request (for demonstration)
    TRANSMIT "Waiting for incoming connection..." TO CONSOLE END
    LISTEN FOR REQUEST STORE IN RAW_DATA END
    
    TRANSMIT "Data received from client:" TO CONSOLE END
    TRANSMIT RAW_DATA TO CONSOLE END
    
    RESPOND WITH WELCOME_MSG END
    TRANSMIT "Response sent. Shutting down." TO CONSOLE END
    
    DEALLOCATE MEMORY END
OTHERWISE
    TRANSMIT "SERVER CRITICAL ERROR: Operation aborted." TO CONSOLE END
END
