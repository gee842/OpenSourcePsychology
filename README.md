# Open Source Psychology
The goal is to use Machine Learning to take in a user's thoughts and feelings, and recommend quotes or ideas from books based on what "disorders" the user may be experiencing

## The Motivation
Everybody is affected by mental health in some way, weather or not it is "diagnosable" according to Psychology literaure is another question. We believe that the way Mental Disorders is viewed in psychology is not condusive to the recovery of everyday undiagnosed sufferers, and also creates a lot of stigma and discrimination for the poeple with labels slapped onto them.

The aim of this project is to try and ease the suffering of people with mental health disorders, even if they don't know they have one yet; Because we believe many people may have traits from different groups of disorders, but it may not be enough to be "Diagnosable", which leads to people not seeking help, or professional psychiatrists not willing to provide help.

We believe this is a problem of how the diagnosis process in psychology inherantly creates stereotypes, stigmas, and preventing people from getting the help they need.

## The Idea
The key idea behind OSP is that there is no "catch all" cure to any one mental health issue, and many people are able to recover through reading and relating to situations similar to themselves, as well as being given the relavant reading and reflective material. 

The core assumption that we are making is that reading about people with similar problems will vastly hasten the recovery from problems people have, as well as ease some of their existential burden. We theorize this effect to be strengthened if the user is then given easy-to-consume tidbits of knowledge relavant to combating their issues (Borrowed from Congnitive Behavioral Therapy)

## The Solution
The ML Model created should be able to corelate an app user's experience with the wealth of experiences shared online, and not only diagnose them (without the biases attatched to the literature of Pyschology), but also provide them with, for example short quotes or testimonials that they may relate to based on the ML-diagnosis.

## Model Decomposition 
This will largely rely on large amounts of data-preprocessing, in order to get a useful, clean dataset to make accurate predictions using a simple word-similarity model on the user input. The idea is that with enough high quality data, keywords in writing style can confidently point the user in the right direction.

![Model Breakdown](https://raw.githubusercontent.com/gee842/OpenSourcePsychology/master/index.jpeg)
