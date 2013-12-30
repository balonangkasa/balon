'''
Created on Dec 23, 2013

@author: pandazen
'''
import mis_compare

ans = True
while ans:
    print("""
    1. Compare form fmb vs fmx
    2. Compare param report
    3. Compare report
    4. Compare file vs database
    5. Compare all
    
    Press enter to quit
    """)
    ans=input("What would you like to do now?")
    if ans=="1":
        print("\nCompare fmb vs fmx")
        mis_compare.fmb_fmx()
    elif ans=="2":
        print("\nCompare param report")
    elif ans=="3":
        print("\nCompare report")
    elif ans=="4":
        print("\nCompare file vs database")
    elif ans=="5":
        print("\nCompare all (1..2..3..4..5)")        
    elif ans!="":
        print("\nNot a valid choice")