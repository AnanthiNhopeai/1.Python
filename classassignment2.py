class SubfieldsInAI():
    def subfields():
        print('Sub-fields in AI are:')
        print('Machine Learning')
        print('Neural Networks')
        print('Vision')
        print('Robotics')
        print('Speech Processing')
        print('Natural Language Processing')

class ODDEVEN():
    def OddEven():
        num=int(input('Enter the number:'))
        if((num%2==0)):
            print(num,'is a Even Number')
            message='Even number'
        else:
            print(num,'is a Odd Number')
            message='Odd Number'
        return message
        
class EligiblityForMarriage():
    def Eligible():
        sex=input('Your Gender(male,female,m,f):')
        age=int(input('Your Age:'))
        if(sex.lower() in('female','f')):
            if(age>=18):
                    print('Eligible')
            else:
                    print('Not Eligible')
        elif(sex.lower() in('male','m')):
            if(age>=21):
                    print('Eligible')
            else:
                    print('Not Eligible')
        else:
                print('invalid input data')
                
class FindPercent():
    def Percentage():
        s1=int(input('Subject1='))
        s2=int(input('Subject2='))
        s3=int(input('Subject3='))
        s4=int(input('Subject4='))
        s5=int(input('Subject5='))
        total=s1+s2+s3+s4+s5
        percentage=(total/500)*100
        print('Total:',total)
        print('Percentage:',percentage)
        
class Triangle():
    def triangle():
        h=int(input('Height:'))
        b=int(input('Breadth:'))
        area=(h*b)/2
        print('Area Formula:(Height*Breadth)/2')
        print('Area of Triangle:',area)
        h1=int(input('Height1:'))
        h2=int(input('Height2:'))
        b1=int(input('Breadth1:'))
        perimeter=h1+h2+b1
        print('Perimeter formula:Height1+Height2+Breadth1')
        print('Perimeter of Triangle:',perimeter)