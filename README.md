# password-cracking
Simple password cracking using wordlist and rules using john the ripper

# install required packages
sudo apt-get -y install git build-essential libssl-dev zlib1g-dev/n

sudo apt-get -y install yasm pkg-config libgmp-dev libpcap-dev libbz2-dev

# download and extract the source code from Openwall github repo
wget https://github.com/openwall/john/archive/bleeding-jumbo.tar.gz

tar -xzvf bleeding-jumbo.tar.gz

configure and install john using 

cd john-bleeding-jumbo/src/

./configure && make -s clean && make -sj4

cd ../run/

# using john

To crack password files using john use './john <file>' replacing <file> with 'passwd-easy'. Can specify rule or wordlist using ./john <password list> --wordlist=<wordlist> --rules=<rules> (./john 101193611 --wordlist = password.lst --rules=best64)

cracked passwords will be printed to terminal and saves in file $JOHN/john.pot. $JOHN/john.pot is also used to not load password hashes that were already cracked for when you run john the next time

To retrieve cracked passwords run ./john --show <password list> (./john --show passwd-easy)

when cracking press any key for the current status or q to abort the session. Use ./john --restore to resume the session.


add cracked passwords to file ./john --show file | cut -d: -f2 | head -n -1 > <filename>

# Given challenge 

From the password list 101193611 find any two users that have identical passwords, two users that have a password palindrome, two users that have a password with prefix 'com' prepended to an anagram.

First run 

./john 101193611 --wordlist=password.lst --rules=best64

this should give you two users who have same password and two users with palindrome. Best64 has a palindrome rule. Add all cracked passwords to new wordlist.

To get two users that have a password with prefix 'com' prepended to an anagram create a new wordlist of anagrams of the previously cracked passwords using anagram.py. Next create a new .rule file part2.rule and add it to the john.conf file. part2.rule has 1 rule that prepends 'com'. Run john with the new anagram wordlist with the newly created rule. 

david and micheal have password: jones071

mary password: aayiH

jones password: Hiyaa

sarah password: comBlah2

jennifer password: comh2Bal
