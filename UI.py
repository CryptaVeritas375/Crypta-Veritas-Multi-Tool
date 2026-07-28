import os
from colorama import Fore
def logo():
    os.system("cls")
    print(Fore.RED + """
    
                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`
[Crypta Veritas - Opens Source Tools]
    """ + Fore.RESET)

def chooses():
    logo()
    print("""
    --------------------------------------------------------------------------
    |    [1]. DNS Lookup | [2]. IpLook UP | [3]. ICMP Flood | [4]. portScann | 
    --------------------------------------------------------------------------
    """)