#include "lists.h"

/**
 * check_cycle - check if a list has a cycle in it
 * @list: list
 *
 * Return: 0 (no cycle), 1 (is a cycle)
 **/
int check_cycle(listint_t *list)
{
	listint_t *data;
	listint_t *dref;

	if (!list || !list->next)
		return (0);

	data = list;
	dref = data->next->next;

	while (data && dref && dref->next)
	{
		if (data == dref)
			return (1);

		dref = dref->next->next;
		data = data->next;

	}
	return (0);
}
