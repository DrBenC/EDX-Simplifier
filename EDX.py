from matplotlib import pyplot as plt

#set the sample name manually
sample_name=input("Type sample name: ")

#we find the computer generated Map Sum Spectrum file and import it
with open("Map Sum Spectrum.txt", "r") as file_raw:
    raw_data = file_raw.readlines()

#here we trim the data by removing the header and footer of the file
data_trimmed=raw_data[49:-1]
energy=[]
intensity=[]

#however now we just have a list of strings - this a crude but functional method
#to reduce these strings into usable floats and putting them in the lists defined above
for n in data_trimmed:
    energy.append(float(n[:7]))
    intensity.append(float(n[9:-2])/10000)

#finally, we plot the spectrum and save it as an image
plt.close()
plt.title("EDX Map Sum Spectrum of "+sample_name)
plt.xlabel("Energy / keV")
plt.ylabel("Counts / x10$^4$")
plt.plot(energy, intensity)
plt.savefig("Map Sum Spectrum.png")

#and for good measure, we save the trimmed, reprocessed data in a format easier to put into Origin
with open("Map Sum Trimmed.txt", "w") as output:
    for n, e in zip(energy, intensity):
            output.write(str(n)+", "+str(e)+"\n")
