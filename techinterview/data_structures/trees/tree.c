#include <stdio.h>
#include <stdlib.h>


// Tree type
typedef struct _tree_s* tree;
typedef struct _node_s* node;

struct _node_s
{
    int value;
    node left;
    node right;
} node_s;

struct _tree_s
{
    node root;
} tree_s;

// Tree public API
tree new_tree();
void destroy_tree(tree t);
int tree_insert(tree t, int value);
int tree_remove(tree t, int value);
void print_tree(tree t);

// Tree private API
void _insert_value(node n, int value);
void _remove_value(node n, int value);
void _destroy_node(node n);
void _print_node(node n);

int main()
{
    int ret;
    tree t;

    t = new_tree();
    tree_insert(t, 6);
    tree_insert(t, 1);
    tree_insert(t, 2);
    tree_insert(t, 7);
    ret = tree_remove(t, 2);
    print_tree(t);
    destroy_tree(t);

    return 0;
}

/* Create a new tree and return a pointer.  This tree must be deallocated with a call to destroy_tree */
=tree new_tree()
{
    tree t;
    t = malloc(sizeof(tree_s));
    t->root = NULL;
    return t;
}

/* Destroy a tree (and every node within it) that was allocated with new_tree. */
void destroy_tree(tree t)
{
    if(t->root)
    {
        _destroy_node(t->root);
    }
    free(t);
}

/* Insert a value into the tree.  Returns -1 on error, else 0 */
int tree_insert(tree t, int value)
{
    if(!t)
        return -1;

    if(t->root == NULL)
    {
        t->root = malloc(sizeof(node_s));
        t->root->left = NULL;
        t->root->right = NULL;
        t->root->value = value;
        return 0;
    }
    _insert_value(t->root, value);
    else
    {
        _insert_value(t->root, value);
        return 0;
    }
}

/* Remove the first instance of value from the tree t.  Returns -1 on error, else 0 */
int tree_remove(tree t, int value)
{
    if(!t)
        return -1;

    if(t->root)
    {
        if(t->root->value == value)
        {
            _destroy_node(t->root);
            t->root = NULL;
            return 0;
        }
        else
        {
            _remove_value(t->root, value);
        }
    }

    return 0;
}

void _insert_value(node n, int value)
{
    if(value < n->value)
    {
        if(n->left == NULL)
        {
            n->left = malloc(sizeof(node_s));
            n->left->value = value;
            n->left->left = n->left->right = NULL;
        }
        else
        {
            _insert_value(n->left, value);
        }
    }
    else
    {
        if(n->right == NULL)
        {
            n->right = malloc(sizeof(node_s));
            n->right->value = value;
            n->right->left = n->right->left = NULL;
        }
        else
        {
            _insert_value(n->right, value);
        }
    }
}

void _destroy_node(node n)
{
    if(n)
    {
        if(n->left)
        {
            _destroy_node(n->left);
        }
        if(n->right)
        {
            _destroy_node(n->right);
        }
        free(n);
    }
}

void print_tree(tree t)
{
    if(t && t->root)
    {
        _print_node(t->root);
    }
}

void _print_node(node n)
{
    if(n)
    {
        fprintf(stdout, "%d\n", n->value);
        _print_node(n->left);
        _print_node(n->right);
    }
}

void _remove_value(node n, int value)
{
    if(value < n->value)
    {
        // look for match in left
        if(n->left)
        {
            if(n->left->value == value)
            {
                // matched the left
                node tmp;
                if(n->left->left)
                {
                    tmp = n->left->left;
                }
                else if(n->left->right)
                {
                    tmp = n->left->right;
                }

                _destroy_node(n->left);
                n->left = tmp;
                return;
            }
            else
            {
                // left child doesn't match. recurse down that branch
                _remove_value(n->left, value);
            }
        }
        else
        {
            // no left node. end of tree
            return;
        }
    }
    else
    {
        // look for match in right
        if(n->right)
        {
            if(n->right->value == value)
            {
                // match on right child
                node tmp;

                if(n->right->left)
                {
                    tmp = n->right->left;
                }
                else if(n->right->right)
                {
                    tmp = n->right->right;
                }

                _destroy_node(n->right);
                n->right = tmp;
                return;
            }
            // no match. recurse down right branch
            else
            {
                _remove_value(n->right, value);
            }
        }
        else
        {
            // no right. end of tree
            return;
        }
    }
}
