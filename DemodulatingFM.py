#jis6cd
#Jessica Shaughnessy

from pylab import *
#import Matplotlib
import numpy as np
#import scipy.signal as signal
import sounddevice as sd
import scipy.io.wavfile as writer

def resampleAndPlayAudio(input):
    #orginal samples where taken at 200kHZ need to down sample to 44.1kHz
    #keep every 4 sample  200kHz /44.1kHz = 4.5
    demodulated = np.angle(input[1:]*np.conj(input[:-1]))
    result = demodulated[::4]
    plt.plot(result)
    sd.play(result,44100)
    writer.write("result.wav", 44100, result)
    plt.show()

def main():
    #Read in the samples:
    incoming_signal = np.loadtxt("IQSamples.txt", dtype=complex)
    resampleAndPlayAudio(incoming_signal)
    ### Polar discriminator
    pass


if __name__== "__main__":
    main()