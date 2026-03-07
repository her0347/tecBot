# TecBot, a the IT department in your computer!


        
def get_response(msg):
    msg = msg.lower()

    # Greetings
    if msg in ["hi", "hello", "hey", "hii", "yo"]:
        return "Hello, I am a chatbot designed to assist with technical issues. Please input a technical issue for me to assist with."
    
    # About bot
    elif "who are you" in msg or "what are you" in msg:
        return "I am a chatbot built to assist you with technical issues. Due to the way I am programmed, sometimes I struggle to understand prompts. Please type 'help' for some keywords and info on how to operate me properly"
    
    # Capabilities
    elif "what can you do" in msg or "purpose" in msg or "designed for" in msg:
        return "I can help assist you with various technical problems, such as a poor internet connectivity, you device not powering on, or device is slower than usual."
    
    # Help
    elif "help" in msg:
        return "Example queries: 'my computer will not turn on', 'my computer is not connecting to the internet', 'my computer is slower than usual' "
    
    # Computer not switching on intent
    elif "computer wont turn on" in msg or "my computer will not turn on" in msg or "computer will not power on" in msg or "not turn on" in msg or "not turning on" in msg:
        return "Is the power connected? If you have a laptop or another device that does not need to be plugged in constantly, check if the battery is dead or run out. Try holding the power button down for a short while until it turns on. Alternatively, try holding the power for a few seconds, then turning it back on normally."
    
    # Computer not connecting to internet intent
    elif "computer is not connected to internet" in msg or "no connection" in msg or "connectivity issues" in msg or "WIFI" in msg or "wifi" in msg:
        return "Try clicking the WIFI icon in the bottom left of your screen and try reconnecting to the WIFI. If that does not work, then try restarting your router or modem."

    # Slow computer intent
    elif "slow computer" in msg or "computer is laggy" in msg or "computer not as fast" in msg or "slow loading" in msg or "my computer is slower than usual" in msg or "computer is slow" in msg:
        return "If you have noticed issues in performance, try clearing hard drive space by either going through your file explorer or using Windows Disk Cleanup (or other trusted application). Also run an antivirus scan using your trusted antivirus software. Malware and crypto miners can cause significant drops in performance. If these come up as clear, check your devices specifications using task manager (Windows). Some applications are more resource intensive than others."
    
    # Cannot connect to printer intent
    elif "computer not connecting to printer" in msg or "printer not working" in msg or "printer" in msg:
        return "If you are having problems with printing, try reconnecting with the printer using a wired connection if possible. You can also install or update the printer drivers manually"

    #General issue intent
    elif "computer wont work" in msg or "my computer won't work properly" in msg or "computer not working" in msg or "computer isn't working" in msg:
        return "Could you please be more specific? I can only help with issues if you tell me what is wrong with the device (e.g. 'my computer will not turn on', 'my computer will not connect to the WIFI'). If you need assistance or are struggling to prompt the assistant correctly, please type 'help' for prompts."
    
     
    # Windows care tips intent
    elif "windows care tips" in msg or "Windows 11 care tips" in msg or "tips" in msg:
        return "to help your Windows PC keep running at optimum efficiency, you can restart your computer regularly, free up space on your hard drive, and keep Windows up to date. For more information, look out for the Windows health tab in your settings"

    #programs crashing intent
    elif "apps crashing" in msg or "apps close" in msg or "apps wont open" in msg or "programs not opening" in msg or "programs crashing" in msg:
        return "Programs crashing on startup is a frustrating problem. Try restarting your device and making sure Windows is up to date. You can also try repairing apps by either going to settings -> add and remove programs and selecting 'modify'. When the installation windows pops up, select repair. You could also just go straight to the install.exe file and select repair through there if it is an option. If all else fails, uninstall and reinstall the program."
    
    #programming language intent
    elif "what programming language were you made in" in msg or "how were you made" in msg or "are you an ai" in msg or "programming language" in msg:
        return "I was programmed in Python. I am what is called a 'rule based' chatbot, so I am not a 'true AI' as I do not learn off experience, but rather rely on preprogrammed messages. This is why I get easily confused if a prompt is unclear or has lots of typos. While my developer has made an effort to make me easy to use and understand various prompt variations, I sill can struggle. On the upside, I don't use loads of water or steal from artists :)"
    
    # source code intent
    elif "source code" in msg or "your code" in msg:
        return "My source code will be available at a later date in the form of a .py file."
    
    # High CPU usage intent
    elif "CPU" in msg or "cpu" in msg or "cpu usage" in msg or "cpu usage too high" in msg:
        return "High CPU usage is often caused by programs using up your processing power. Try using Task Manager to clear up CPU usage by closing apps. You could also try restarting your computer. It would also be worth doing a scan with your antivirus to catch any malware that may be causing your system more strain."
    
    # bluetooth intent
    elif "bluetooth isn't working" in msg or "bluetooth connectivity issues" in msg or "bluetooth" in msg:
        return "try turning the Bluetooth on and off in your settings."

    # High RAM usage intent
    elif "RAM" in msg or "ram" in msg or "high ram usage" in msg or "high RAM usage" in msg or "ram usage" in msg or "RAM usage" in msg:
        return "If your RAM usage is high, try closing programs and unnecessary processes. If you are doing something on a regular bases that pushes you computer to its limits or it cannot handle it, consider upgrading individual components, or upgrading altogether if upgrading components is not possible (e.g. RAM soldered in a laptop)."
    
    # Overheating intent
    elif "computer is overheating" in msg or "computer getting too hot" in msg or "too hot" in msg or "computer overheating" in msg:
        return "There are many potential reasons why your computer is overheating. The first reason is you are just doing heavy work that is pushing your computer a little harder than usual (e.g. gaming, exporting files, intensive software) or something else. First, try freeing up some RAM in task manager or properly shutting down your computer and leaving it for a while. Overheating only ever signals something may not be right of your computer begins overheating soon after you start your computer. Serious overheating will cause your computer to 'throttle', meaning it will deliberately slow down the CPU and GPU (used to run processes and display images respectively) to try to cool down. Sometimes overheating can be a sign your PC or laptop's fans have been blocked or there is a buildup of dust. If you can safely clean out the dust yourself, then clean it yourself. HOwever this may be more difficult on a laptop than a desktop. If the inside is damaged, it may be worth getting it professionally repaired, or potentially replaced if the cost of upgrading or replacing is less than that of repairing."
    
    # Exit conditions
    elif msg in ["bye", "exit", "quit", "goodbye"]:
        return "exit" # signal to break loop
    
    # Fallback
    else:
        return "I don't understand, please try a different prompt. New issues are being added all the time, so for the time being, please search on the web to find a solution"
    
def start_chat():
    print("TecBot session connected. Type 'exit' to stop. Type 'help' for assistance in operation of the bot and key phrases that can be used.\n")

    while True:
        user = input("User: ").strip()

        if not user:
            print("TecBot : Please type something.")
            continue
        
        response =get_response(user)

        if response == "exit":
            print("TecBot : Session terminated.")
            break
        
        print("TecBot:", response)

if __name__ == "__main__":
    start_chat()
    
