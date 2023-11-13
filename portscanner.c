#include <stdio.h>
#include <stdbool.h>
#ifdef __WIN32__
# include <winsock2.h>
#else
# include <sys/socket.h>
#endif


int main(int argc, char *argv[])
{
    int starting_port;
    int ending_port;
    int i;
    int ip;
    
    if (argc != 4)
    {
        printf("Usage: %s <ip> <starting port> <ending port>\n", argv[0]);
        return 1;
    }

    ip = inet_addr(argv[1]);
    starting_port = atoi(argv[2]);
    ending_port = atoi(argv[3]);

    for (i = starting_port; i <= ending_port; i++)
    {
        int sock = socket(AF_INET, SOCK_STREAM, 0);
        struct sockaddr_in addr;
        addr.sin_family = AF_INET;
        addr.sin_port = htons(i);
        addr.sin_addr.s_addr = ip;

        if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == 0)
        {
            printf("Port %d is open\n", i);
        }
        close(sock);
    }
    
    return 0;
}