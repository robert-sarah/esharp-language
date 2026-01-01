SECURE
    # 1. Mandatory Memory Allocation - The first step to complexity
    ALLOCATE MEMORY FOR EXECUTION END
    
    TRANSMIT "--- E# Tutorial: The Complex Simplicity ---" TO CONSOLE END
    TRANSMIT "Memory successfully allocated." TO CONSOLE END

    # 2. Variable Establishment - Verbose and strict
    ESTABLISH INTEGER BASE_VALUE AS 5 END
    ESTABLISH RESISTANT INTEGER RESISTANCE_FACTOR AS 100 END
    ESTABLISH STRING MESSAGE AS "The result is: " END
    
    # 3. Calculation - Prefix notation for maximum difficulty
    CALCULATE ADD WITH BASE_VALUE AND RESISTANCE_FACTOR STORE IN INTERMEDIATE_RESULT END
    
    # 4. Output
    TRANSMIT MESSAGE TO CONSOLE END
    TRANSMIT INTERMEDIATE_RESULT TO CONSOLE END
    
    # 5. Robustness Test - Attempting to violate the resistance principle
    SECURE
        TRANSMIT "Attempting to change RESISTANCE_FACTOR..." TO CONSOLE END
        ESTABLISH INTEGER RESISTANCE_FACTOR AS 1 END # This will fail
    OTHERWISE
        TRANSMIT "RESISTANCE_FACTOR is resistant. Error handled gracefully." TO CONSOLE END
    END
    
    # 6. Mandatory Memory Deallocation - Clean up is complex too
    TRANSMIT "Memory successfully deallocated. Program terminated." TO CONSOLE END
    DEALLOCATE MEMORY END

OTHERWISE
    TRANSMIT "CRITICAL FAILURE: The entire program failed to execute." TO CONSOLE END
END
