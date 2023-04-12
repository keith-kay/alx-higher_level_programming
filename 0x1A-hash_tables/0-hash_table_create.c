#include "hash_tables.h"
#include <stdlib.h>

/**
 * hash_table_create - Creates a new hash table.
 * @size: The size of the hash table.
 *
 * Return: A pointer to the new hash table, or NULL on failure.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *t = NULL;
	unsigned long int i;

	t = malloc(sizeof(*t));
	if (t == NULL)
		return (NULL);

	t->array = malloc(sizeof(*t->array) * size);
	if (t->array == NULL)
	{
		free(t);
		return (NULL);
	}

	for (i = 0; i < size; i++)
		t->array[i] = NULL;

	t->size = size;

	return (t);
}
