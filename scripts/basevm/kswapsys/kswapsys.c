#include <stdio.h>
#include <libgen.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

void do_swap(char *from, char *to) {
    if (rename(from, to) == -1) {
        printf("Cannot rename %s to %s: %s.\n", from, to, strerror(errno));
        exit(1);
    }
}

int main(int argc, char **argv) {
    int i;
    char *old_sys_dir, *new_sys_dir;
    
    if (argc < 4) {
        printf("Usage: kswapsys <old_sys_dir> <new_sys_dir> <swap_path_1>, <swap_path_2>, ...\n");
        return 1;
    }
    
    old_sys_dir = argv[1];
    new_sys_dir = argv[2];
    
    for (i = 0; i < argc - 3; i++) {
        char *swap_dir = argv[i + 3];
        char tmp[512], old_path[512], new_path[512], *swap_name;
        strcpy(tmp, swap_dir);
        swap_name = basename(tmp);
        sprintf(old_path, "%s/%s", old_sys_dir, swap_name);
        sprintf(new_path, "%s/%s", new_sys_dir, swap_name);
        do_swap(swap_dir, old_path);
        do_swap(new_path, swap_dir);
    }
    
    return 0;
}

