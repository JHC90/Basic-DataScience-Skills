# Read-Me

Ziel ist es hier nur mal Tensorboard zum laufen zu bringen, und das hat soweit so auch geklappt.

hier ist eine Beispiel implementierung von dem Tensorboard. Das ganze wurde nach dem Tutorial von "https://medium.com/@kapilvarshney/how-to-plot-the-model-training-in-keras-using-custom-callback-function-and-using-tensorboard-41e4ce3cb401" durchgeführt.

* starte eine env (da wo logischerweise die Packete installiert sind)
* definiere ein Log verzeichnis auf welchem
    * Tensorboard gestartet wird
    * im Script file die logs auch hingespeichert werden
* starte Tensorboard via Konstolenaufruf 
  >(Kompensationsarbeit) C:\Users\1810837475\Desktop\Basic-DataScience-Skills\NNs\Tensorboard>tensorboard --logdir=./logs

  => hier kommt zusätzlich eine URL auf welcher ich dann tensorboard im Browser öffnen kann
* Starte das Script, und im Browser werden automatisch die akutellen Stati von dem NN angezeigt
