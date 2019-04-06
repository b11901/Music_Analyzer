import os
import subprocess
import numpy as np
import scipy.io.wavfile
import ntpath
import matplotlib.pyplot as plt

def analyze(song,newSong,a,b):
    #name = create_wav_file(song)
    rate,audData = scipy.io.wavfile.read("songs/wav/second.wav")
    channel = audData[:,0] #left channel
    
    CHUNK = 1024

    a += CHUNK
    b += CHUNK
    print(a,b)

    print(len(channel))

    fft_data = np.fft.fft(channel[a:b])
    freq = np.absolute(fft_data)
    freq = freq[freq <= 25000]
    sorted_freq = np.sort(freq)
    #print(sorted_freq)
    #sorted_freq = sorted_freq
    #print(sorted_freq)

    r1 = int(( sorted_freq[0] / 22000 ) * 100)
    r2 = int(( sorted_freq[int(len(sorted_freq)/2)+50] / 22000 ) * 100)
    r3 = int(( sorted_freq.max()/ 22000) * 100)

    return r1,r2,r3

def create_wav_file(song):
    song_name = ntpath.basename(song) #Find out the actual name of the file rather than its path
    bash_command = "ffmpeg -i " + song_name + " temp.wav"
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return "temp.wav"

def analyzerRect():
    rate,audData = scipy.io.wavfile.read("songs/wav/second.wav")
    channel = audData[:,0] #left channel
    Pxx, freqs, bins, im = plt.specgram(channel, Fs=rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

    
    np.where(freqs==10034.47265625)
    data=Pxx[233,:]
    a = data[data>2500]
    return a[0:60]
