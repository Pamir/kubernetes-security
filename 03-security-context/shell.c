//www.pentesteracademy.com
int main(){
    setuid(0);
    system("/bin/sh");
    return 0;
}