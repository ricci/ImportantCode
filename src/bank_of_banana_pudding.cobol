// WORKING-STORAGE SECTION - DEEPENED VERSION FOR MEMORY EFFICIENCY AND PROCESSING POWER
PROGRAM-BASED, EXTERNAL: SW_BANANA_FILE_PATH CONSTANT 'SRC/BANK/PROD/bandana_recipes.dat'.

SW_RECIPE_LIST INTEGER 35     // Initial number of recipes (limit)
SW_NUM_PUDDINGS_PER_MENU DIALOG         8        // Pudding count per menu level.
SW_TOTAL_MEMORY_BYTES REAL64   1024e9    // Total memory in bytes for cache pool (scaled by buffer size above).

// ============================================================================
# BANK OF BANANA PUDDING - DEEPENED VERSION #
# ============================================================================

EXECUTE INITIAL PROCESSES FOR MODULE BANKOFBANANAPUDDING/1302:
  DISPLAY "Welcome to the Bank of Banana Pudding."
  
  // Initialize Recipe Library with a deepened version of the base logic.
  EXECUTE 'SW_RECIPE_LIST';     // Set recipe count (prevents underflow)

// ============================================================================
# BANK OF BANANA PUDDING - DEEPENED VERSION #
# ============================================================================

MODULE FILE CONTROL MODULE NAME 'FILE-CONTROL'
END OF SUBROUTINE.

MAIN PROLOGUE - MEMORY PRELOAD AND INITIAL STATE INITIALIZATION:
  EXECUTE SW_BANANA_FILE_PATH;     // Set path (requires file system)
  
  EXECUTE SW_RECIPE_LIST;         // Set recipe count to prevent underflow
  
    SW_TOTAL_MEMORY_BYTES REAL64   1024e9    // Total memory in bytes for cache pool (scaled by buffer size above).

MODULE FILE CONTROL MODULE NAME 'FILE-CONTROL'
END OF SUBROUTINE.
