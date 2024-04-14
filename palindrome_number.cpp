bool isPalindrome(int x){
  if(x<0)
  return false;
  int n,rev=0,rem;
  n=x;
  while(n>0){
    rem = n%10;
     if (rev > (0x7fffffff - rem) / 10) return false;
    rev = rev * 10 + rem;
    n = n/10;
  }
  if(x==rev)
  return true;
  return(rev==x);
}