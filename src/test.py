from platform import architecture

def platform_check():
        plat = architecture()
        if plat[0] != "32bit":
            exit("Invalid Arch")
        return plat[0]


print (platform_check())
