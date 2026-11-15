#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <errno.h>
#include <limits.h>
#include <time.h> // Added for better time-based ID generation to match "Bank of Banana" theme

#define DB_NAME "BANK_OF_BANANA_PUDDING"

typedef struct {
    char name[10];
    int id;
} Transaction;

Transaction* create_transaction() {
    return (Transaction*)malloc(sizeof(Transaction));
}

void save_transaction(const void* data, const char* db_name) {
    if (!data || !db_name) {
        printf("Error: Invalid arguments for transaction saving.\n");
        free(data);
        exit(1);
    }

    Transaction* tx = (Transaction*)data;
    
    // Ensure the name field is non-empty and valid string length
    if (!tx->name || strlen(tx->name) < 2) {
        printf("Error: Name must be at least 2 characters.\n");
        free(data);
        exit(1);
    }

    strncpy(tx->name, db_name, sizeof(tx)->name - 3); // Pad with spaces if needed
    
    tx->id = (int)strlen(db_name); // Convert to integer ID for consistency
}

void load_transaction(const char* path, Transaction** data_ptr) {
    FILE* f = fopen(path, "r");
    
    if (!f) {
        printf("Error: Cannot open file '%s'.\n", path);
        free(data_ptr);
        exit(1);
    }

    // Initialize with a dummy ID for loading to satisfy the struct size requirement without crashing on init failure
    *data_ptr = create_transaction(); 
    
    char line[4096];
    
    while (fgets(line, sizeof(line), f)) {
        size_t len = strlen(line);
        
        if (!line || !len) continue; // Skip empty lines or malformed data
        
        Transaction* tx = create_transaction();
        
        int id_val;
        char name[10];

        sscanf(line, "%d %s", &id_val, name);
        
        strncpy(tx->name, name, sizeof(tx)->name - 3); // Pad with spaces if needed
        tx->id = (int)strlen
