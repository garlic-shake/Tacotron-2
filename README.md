# Tacotron-2:
Tensorflow implementation of DeepMind's Tacotron-2. A deep neural network architecture described in this paper: [Natural TTS synthesis by conditioning Wavenet on MEL spectogram predictions](https://arxiv.org/pdf/1712.05884.pdf)


# Dataset:
Для обучения модели использовался [M-AILABS Russian speech dataset](https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/) содержащий 9ч 58м записи речи.

# Результаты:
Результаты обучения модели после 200000 шагов.

Фразы из обучающей выборки:
[1 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_0_sentence_0-linear.wav)
[1 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_0_sentence_0-mel.wav)
[2 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_1_sentence_0-linear.wav)
[2 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_1_sentence_0-mel.wav)
[3 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_2_sentence_0-linear.wav)
[3 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_2_sentence_0-mel.wav)
[4 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_3_sentence_0-linear.wav)
[4 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_3_sentence_0-mel.wav)

Фразы, не содежращиеся в наборе данных для обучения:
[1 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_4_sentence_0-linear.wav)
[1 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_4_sentence_0-mel.wav)
[2 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_5_sentence_0-linear.wav)
[2 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_5_sentence_0-mel.wav)
[3 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_6_sentence_0-linear.wav)
[3 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_6_sentence_0-mel.wav)
[4 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_7_sentence_0-linear.wav)
[4 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_7_sentence_0-mel.wav)
[5 linear](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_8_sentence_0-linear.wav)
[5 mel](https://github.com/garlic-shake/Tacotron-2/raw/master/tacotron_output/logs-eval/wavs/wav-batch_8_sentence_0-mel.wav)


