# QC Foundations [2/4] — Your First Quantum Speedup

**Course:** Quantum Computing — CEP, IIT Delhi  
**Lecturer:** Prof. Kolin Paul, Department of Computer Science and Engineering  
**Date:** 24 October 2026 (afternoon session)  
**Source:** `02 QC Foundations Part B(1).txt`  
**Slide reference:** `02 QC Foundations Part B.pdf` (30 numbered slides, supplied as a 10-page PDF)

> **Transcription policy:** This is a corrected version of the supplied speech-to-text transcript, **not** a summary and **not** a verbatim audio verification. The professor’s explanations, audience exchanges, demonstrations and sequence are retained. Obvious terminology is corrected against the slides. Slide-only material is not inserted as spoken dialogue. Uncertain or internally inconsistent spoken statements are preserved and identified in the editorial notes below. No audio file was supplied.

## Editorial notes on uncertainties and spoken slips

- The transcript starts mid-sentence (“quantum algorithm…”); the preceding words are **not available** and have not been reconstructed.
- The slides use **HZH = X**, and the final Deutsch readout convention **0 → constant; 1 → balanced** (slides 2, 14–18). The speaker briefly reverses these outcomes and immediately self-corrects in the supplied transcript; both statements remain visible in context.
- For **n input bits**, the slides give the deterministic classical worst-case bound **2^(n−1) + 1 queries**, versus **one quantum query** (slides 25–26). The transcript sometimes says “n/2 + 1” or treats n bits as n candidate inputs; those occurrences are preserved as speech rather than silently changed.
- The slide deck labels the extension **Deutsch–Jozsa**. The speech sometimes loosely calls it the Deutsch algorithm; both are retained where context permits.
- Some portions of the live Quirk/Qiskit demo rely on unrecorded screen actions, and a few resulting transcript phrases remain uncertain. They are not supplemented with invented actions.
- The PDF is complete as provided, but a slide match does **not** establish that every sentence was spoken exactly as transcribed.

---

## Introduction and recap from the morning

quantum algorithm so that it makes sense for you to actually appreciate why this is important, why this is actually making the trend and why people are actually investing in it. Remember many of the things that we will do initially for the first half of the course would be mostly in terms of the algebra, et cetera, the key or say or sometimes intuition. But most of or a simulator, as we will show today later in the class. But remember, many of these things have been implemented. And there are things which are working at, say, hundreds of qubits level. OK, so it is there to stay.

And whether we will be able to make money out of it as of now is not very clear. But. at least it is important from both a research perspective as well as the future of where computing is. Okay, so let's just do a quick recap of what we tried to do in the morning. We said that there is this thing called a gate and that gate is an unitary operator, operator is a matrix and some of these gates do some nice things. Correct? So The H gate particularly was doing a superposition for you.

That is my pin. The H was super, was giving you a superposition of 0 and 1. Start with the classical state 0 and you get 0 and 1, which essentially moves things from the North Pole to the equator. And if you do two H's, that was the key thing that you actually are able to go back to the previous state. Okay, so this is different from a random the coin toss and the HZH was actually equal to X. So combination of gates is able to give you a different gate.

Okay, so interference is key superposition and we had just started with this CNOT which was entanglement. I deliberately left it less detailed because To do anything significant out there, obviously I don't have the Bloch sphere as my prop. With a single qubit, I had the Bloch sphere as the prop and therefore I could point you to that and give you some intuitive fill. But with two qubit sort of things, it's not possible to do it on a single cube at a visual level. So you have to do the algebra.

So I just introduced a little bit of the algebra, but unless you do a little bit more on the linear algebra side things that I speak of might actually not be, will not sink in. So we will wait for a week and then we will do the more detailed formal analysis once it finishes with the linear algebra part of it. Okay, so the last row is important. The key thing is that the Z out here determines whether you read a 0 or 1, correct, the phase information. Whether you have landed on a plus state or a minus state and the plus state or minus state is distinguishable. So this is the thing that.

## The fair-coin and trick-coin puzzle

So let us look at another game. We started the first lecture with the coin toss. Now we want to look at again another problem which is again involves coins. One of the things that as faculty we do is that we try and bring in examples from which are not necessarily given in a book. We build our own ones or we actually pick up from many different sources. So therefore this is probably not there in many books.

In fact, some or in some literature you'll find there will be a statement later they have actually also done an incorrect interpretation. So you have to be very careful about what you pick up from the internet. Okay, so. The thing is that we want to figure out whether a coin is actually biased or fair. So what do you mean by a biased fair? The best example or the worst case biased case thing is that as in Sholay both faces have the same side or both faces have the same H or either H or T.

Correct? The famous Sholay thief. Okay. Now the thing is that someone gives you that coin. and with a face up. Now how do you know it is the coin is going to be is fair or it's for and got biased as a trick coin. Okay so now the setting of this is like this correct you are going to toss some the person is going to toss the coin but you don't you want you would like to know whether it is biased or not.

Okay. So, um, and the thing is that every time you look at the coin, you actually have to pay him some money. Okay. So because after that, you're going to play cards with it. Okay. Or something you're going to play a game with it where you might get money, to figure out whether it is biased or not, you want to have to pay him something.

So you want to be exactly sure. Okay. So what do you do? Okay. So you would like to flip the coin, see the coin. Okay. But if you see the coin, And with one look you cannot figure out correct that whether it is biased or not because you have two sides correct you see a head you doesn't tell you that the other one is going to be tail because you can have a head and then you can again have head on the other side.

So that's the key problem that we want to solve. We want to see whether the coin is giving you the same output always or it changes. So therefore you need two looks. Okay, you're not bothered about whether they are both heads or both tails. That is not important. I just want to figure out this condition that they are complimentary, both sides. Okay. And they are. or they are of the same color or the same, same either head or tails.

So, let us start. So, that is the problem we want to really look at. And the teaser is this that if you have a quantum algorithm, you can do it with one look. We will define what that look is, but you can do it with one look. So, that means instead of two, you are doing with one.

## The black box: four possible functions

So we define, so any input that we have, so typically we say that when we have, when we use the word function, okay, it takes an input X and gives me maps it to a function Y, okay? So to a variable value Y. Get an input X, maps, you apply F on it, you get output Y, okay? So this F. takes an input from 0 and 1 and maps it to again 0 and 1. So it gives you an output which is f of x. I'm not bothered about how f is implemented.

I am just saying that f gives you a certain value. And if you have, what are the possible functions that this can have? So we can actually have it something like this, correct? This is something again probably what we learn first thing in digit in Boolean logic that my input can be 0 and 1, 0 or 1. And what can be my output? My output f can be always 0, it can be always 1 or it can be 0, 1.

So these are the possible functions that this box can implement. These are the four possible functions it can implement for a two valued single input. So x belongs to 0 and 1, y also belongs to 0 and 1, therefore they are one bit outputs or one bit inputs and the four possible functions are this. So this is always 0, this is always 1 and this is copy 0 to 1 and you flip last one. So this category is constant, no matter what the input is, you will get only one output. So this is a constant.

This on the other hand is a balanced example of a balanced output. In this particular case, equal number of zeros and ones. In this case, particularly, there is a single one and a single zero in your possible outputs. So if you see, if you go back to the previous problem, your x belongs to H and T, and your y also belongs to H and T. you are trying to figure out what this that whether coin is has this property or has this property.

So, if it has this property, if it has this property that means for all possible values of input that means with h also you will get this with t also you will get this or you might get tt and tt. So, anytime you look your making an observation, you are observing it, so you get a value, the head or the tail. So, whereas you would like to get them as ht or th. So that would be, you want to decide whether the function is constant or balanced. So, and the only thing that you can do is feed inputs and read outputs. You cannot open this box.

## The classical solution: two oracle queries

So the box is an oracle. You want to figure out whether the, so the classical computer can query this box. You read in, in x, you read f of x. So you want to be able to figure out which of those four functions is the oracle implementing. And the promise is that the functions will either belong to the constant category or to the balanced category. So, the promise is this function belongs to the balanced category or the constant category.

And I do need to know whether it is balanced in a 0, 0 or 1, 1. So, the two candidates out here are 0 and 1. Correct? That the function always outputs a 0 or a function always outputs a 1. Or I do need to know whether it is the copy function or the flip function. There are 4 functions out here. So, always 0 always 1, I do need to know whether it is 0 or 1.

I do also need whether it is copy or flip. I just need to know whether the function is constant or not. That means I need to be able to tell whether it always gives a 0, always gives a 1 or sometimes 0. or it gives 0 or 1 for different inputs. Now, classically, what will I do? Classically, what will I do? I will give input 0 to the box.

I will see the answer. If it is 0, I will wait. I will give a 1, and then I will see what the output is. If it is 0, I say it is balanced. If it is 1, I know that it is. If I get a 0, I know it is constant. If I get a 1, I know it is balanced. So therefore, I need two queries. for it to be for me to assert that the box is implementing either a function or which is balanced or is it constant.

No, there's nothing to do with the cat. We are still in maths. So this is computer science. So the Schrodinger's cat was probably the superposition part. Let me not get there. So you query with the input 0. Suppose you get 0, if it's always 0, will, what are the possibilities? The possibilities are that these two are possible, correct? So, can get an output, next output can also be 0, next output with 1, the output can still be 0 and the output can be 1.

So, therefore, both of these possibilities exist and therefore, you must actually query it once more. So, then you need to query it twice. So this is an important thing.

## The quantum promise and the n-bit comparison

suppose I have a function, a function which is again an n-bit function. And it gives me a one-bit answer. How many queries do I need? So suppose I have, so suppose n is equal to five, okay. Let's make it six. So my balance condition will be all zeros and let's come to that later. Next, I cannot confuse you. Okay, so this is an example of an algorithm which will require two queries, okay.

My claim is, or our claim is that, it will need only one query. And this is what I was trying to go at, that even for n-bit inputs, it will still need one query. The condition is that it is now checking, it is telling you basically whether the function is balanced or constant. So it's essentially counting whether the number of zeros is equal to the number of ones that's balanced in the input and whether output is always 0 or always. That means the input string is all 0s or input string is all 1s. That's the only problem that it is solving.

You might ask what is the use of such an algorithm? What is this? Is this even a valid problem? It is a valid problem in terms of maths, in terms of computer science. It is a valid problem. It shows that you have a linear time algorithm. So, to do the n bits one, you have to actually query n by 2 times, n by 2 plus 1 times to be able to figure out whether your function is 0 or 1.

Basically, whether it is constant or balanced. Because suppose you are working with 6 bits, 6 bits, correct? So, this for each bit, you figure out what the output is 0. So, till about 3 bits, if you have seen, it is all 0, the fourth bit might actually be a 1. So, you want to distinguish between these two. So this is actually a balanced, this thing.

So this is constant, this is a balanced input, equal number of zeros and equal number of ones. Okay. And so this, I would need N by two plus one, which is six by two plus one comparisons to be able to figure out whether it is balanced. So this also I can do in a quantum algorithm with just a single query. So you have got a linear time algorithm, which you are able to do in constant time ok. So, that means order of n becomes order of 1.

So, that means this is a linear speed up in terms of computational power. So, this is the reason why quantum algorithms are studied ok. There are other algorithms that you study later which gives from exponential to polynomial which is great ok. So, exponential to half exponential that is another one that we will see, but this is the first one which came around by at some point in time 1985. It's the first quantum algorithm which showed that you can get a speed up. So it's not, it is a question about the box.

That means a function and it let interference produce the answer. It does not read both inputs and produce both outputs and lets you choose. That's not the reason. That's not what quantum algorithms are about. We will see interference is what gives us the answer with a single query. So the idea is to make the box quantum, build the circuit, and see why it works.

That's what this class. So I'll go about this very slowly, because this is where we're a leap of faith. And this is where things become a little bit, as they say,

## Making the oracle reversible

The first thing is we want to make the box quantum. Remember that Oracle box that was evaluating functions, we want to just say. And quantum gates are rotations. And every rotation can be undone. You rotate plus direction, you take it the other way, direction. So that's the first thing we need to keep in mind. We have to work with reversible logic. So that's one.

So what we can do is you can actually take help of. because we want to, no, reversible logic is not backtracking in DSM. Because there's a physics involved in it also because reversible logic amount of energy that you spend while going in the forward direction, you give up the same amount of energy while you're coming back. Number one. Number two is that reversible logic straight away implies that you are going to have the same number of inputs as outputs because you want to operate the circuit from the other side also. So, for example, in this block, I have done 0, 1, always 0, correct? Now, that is the first function, correct?

It's example of a constant function. For either input, the output is always 0. So, you cannot actually figure out what was your input. So, it cannot be a reversible circuit. So, therefore, to make this reversible, if you have two inputs out here, you must have two outputs. So, two inputs, two outputs. So, that's the first thing that if you want to make it reversible.

Okay, so now the intuition must be that what is balanced versus so just I said that correct just think of the equal numbers of ones and zeros is balanced and how all zeros or all ones are in the input means that it is constant. We are completely in classical still now in the definition of the problem. I gave you a linear time algorithm correct so therefore it is all I am asking or saying is that we are trying to figure out that the input contains all zeros or all ones that is constant and or the input has equal number of ones and zeros. So now first I have to make this box quantum correct make it reversible correct.

So to make it reversible I must have two inputs and two outputs. So there are two inputs input and I actually say and I have this box which is now going to do the function evaluation. So my input is a single qubit, correct? A single bit, correct? 0 or 1, correct? So that goes into x. So I'm going to do something that will preserve my input, but I will change only if a certain condition is fulfilled on the other line.

So that's going to be my oracle. In this particular case, have written that I am going to actually whatever is there on the helper line, I am going to flip it if f of x is equal to 1. So that is still classical, there is no quantum involved out here. I have just drawn a diagram with a behavior. I am saying the first line just copies things. That means y is equal to x in the first line.

In the second line, y is equal to not of h. So what I'm saying is that this and this is a copy. And if I say this and this h, so what y is equal to not of h if this condition is satisfied. So we'll look at this later. So essentially what we are saying is that you have x out here and you have y out here. So x and y changes to x. this remains as x, this changes to y exclusive or f of x.

So that is the meaning. So this is just in the ket notation or in the tensor notation, we will actually look at it. And this condition flipped is essentially the XOR function. If you look at the truth table of XOR, if you have x and y, 0 0 0 1 1 0 1 1, the output f will be this is 0, this is 0 and only here do you get, if they actually are different you get a 1. So, this condition can be encapsulated by this.

## The four quantum oracle circuits

So, now I want to see if I can make those, so I want to make this block box correct and I want to be able to define these four functions. So, always 0, x and h nothing happens correct? The x remains as x. Always 1, again x remains as x. And h always flips. So, if you want to do a copy flip if x is equal to 1, remember h could have started with 0, if x is 0 let it remain as 0.

If x is equal to 1, you change it to 1. because that's the copy function, correct? And the flip function is you do the same thing but have an inverter in front. So the balanced oracles need a CNOT. The helper's fate depends on X. So this is a very simple circuit, but in general, this black box, in this oracle black box can actually be a very complicated circuit requiring many gates, but we're not. bothered about that for the time being we know that there is a function block which gives me that answer. Whether when I give an input it tells me whether the output is 0 or 1, how it does that not bother.

So, this is one thing that this basically defines what the problem is and how can we get this. to be evaluated by a quantum circuit using the gates that I have already introduced.

## Quantum parallelism—and why measuring is not enough

So the second thing that I want to be able to do is to be able to exploit this notion of parallelism. One of the things that you hear about in the hype about quantum computing is that everything is done in parallel. It really is not that simple. In fact, that is a pretty wrong interpretation. But there is parallelism somewhere, otherwise how do I get my results? I am able to do two queries, instead of doing two queries, I am doing it in one, instead of n queries, n by 2 plus 1 queries, I am doing it in one and I getting the answer.

So, there is some degree of parallelism somewhere. let us look at it. So, if you are on the equator, so suppose. what there are two lanes for example say the I pass the data along those two lines and then the oracle holds f of zero the helper holds f of zero and with x equal to one the helper will hold f of one from this diagram okay okay so if you see both answers are in the in the result of the oracle. Because remember you have built a two input two output circuit. So you have this circuit and what are we saying? We are saying this, correct? That here you might have given him a plus state.

Remember the plus state is what? Plus state is 0 plus 1 over root. So, which essentially means you have given him two paths, correct? There is a zero path and there is a one path. So, for the zero nothing happens, zero remains a zero. For the one path, he will actually, whatever is out here will be flipped. So, that means the information content will be here for the one part.

So, that is the important thing that you have to remember. That is the parallelism part that is happening. So, the x equal to zero holds the F0 part and x equal to 1 holds the F of 1 part. So this two qubit system contains both your F0 and F of 1. Because remember you have not sent in 0 or 1. You have sent him a plus state.

If you have sent him a plus state, the plus state contains 0 and 1. And hence the result in one part you will have F of 0 and in the other part you would have F of 1. assuming this box is doing f. Oracle is basically a function. The Oracle is actually a physical unit, piece of software and define, all of them are true. But it's being executed, you are building a circuit, correct? If I'm building a circuit clearly, it'll be there.

It's just that it might be very complex, but for the example that I'm doing is actually a very simple one. I've drawn the four functions, correct? So now you have the ans, f of 0 here and f of 1 here. Now if you do a measurement, you will find both probabilities half, you do not get anything. So you can measure any one state at any given time and that gives you 50 % probability. So it is worse than classical.

So the key idea then is that I cannot actually extract this information. is still in the two, it's in the two qubits or the two lines correct. Each of those lines represents a qubit. So you cannot actually extract individual qubit information. So I'll have to do something so that these two lines interfere with each other and give me a more definite answer. So parallelism by definition is not good enough. parallelism on its own is not good enough. You need to be able to do interference to be able to get a correct result.

## Phase kickback: the CNOT experiment

So how do we do this interference? Remember we had this entangled business. So before even looking at entangle, just look at it from a classical perspective also. So what am I saying? I'm saying that I'm going to use a CNOT. A CNOT is something which actually works on two bits. at the same time. One of those bits actually remains unchanged. The other one changes its condition or flips depending on whether the first one had a 1 or not.

So the control bit is more like a read bit for the target qubit. that's correct. So now if you look at the control qubit, so if the control qubit I said in terms of 1 and 0, correct. Now I am saying the control qubit is plus, which essentially means this is 0 plus 1 by root 2 and I am applying it on 0 minus 1 root 2. And then you go and apply the linear property, that is what he said, operators are linear operators, CNOT is also a gate, a gate is a unitary operator. So, if you look at this, what it essentially means, if it is 0, nothing The zero part will not change this.

It will remain as it is. The one part will go and flip this one. So this is the important thing. The zero will not do anything, the one part. But then remember this one, the control has both zero and one. So the target also, some parts will be affected, some parts will not be affected. if you're controlling the equator, so now think about it in terms of the...

So, there would be for the two qubits there are two arrows correct. So, only one arrow will actually move correct, which is essentially the target one. Which was the intuitive ones, but if you see, so the control is with and then you do a CNOT, the plus moves. These are the two and then the target comes here, the CNOT goes there. So, the control move the target does not. The CNOT flips the target, but still the CNOT stays wherever it is, the control goes from plus to minus.

So this is the most important part of this lecture. So I want you to actually do the maths or don't do the maths, just see what is happening to write out the equations and see what happens. This is very important. So till now, what have we said? So if I have a, so this is my CNOT, correct? So this is X, this is Y.

Okay. And this output was going to be X and the, output was going to be Y exclusive or F of X. This comes from this slide. Okay. So X remains as X and Y becomes you flip. if f of x is equal to 1. So this is you flip y is flipped if f of x is equal to 1. What is f of x if basically whether x is equal to 0 or 1.

So now, so let's remove this also make it simpler. So now if I do this, if this was 0 and this is 1, this remains as 0. this remains as 1. We agree because we are not going to do anything to y because f of because x is equal to 0. Now if I change this to 1 and leave this as 1, this will become this will still be 1 and this will become 0. With 0 and 0, this will still remain 0. With 1 and 0, this will become 0 and 1.

We agree that this is what a controlled-NOT does. The knot operation is happening based on the control. Key thing is nothing is happening here. This remains as it is. agree? So now what are we saying? Now we are saying that on this I'm going to give a plus and on this I will have a minus. And our plus is defined as this and a minus is defined with the minus sign.

So if we had followed the intuitive answer plus would have remained as plus and something would have happened to minus. That's basically the question out here. And the claim is that the target does not move, the control will move.

## Why the control changes while the target stays put

So if you look at the control, is I can do it maths, but let's do the intuition first. So the control plus is a zero branch and a one branch side by side. Correct? This is one way of looking at it. is a plus and a minus, a plus and a zero and a one coming together. So plus is a zero and one coming together. The CNOT only acts on the plus on the one branch, it applies x to the target there.

So what was our circuit? So control is here. whenever there is a one out here, it will apply something on the negative thing. So the target is this, it is on the x-axis. The flip cannot move it, just gets you a minus sign. Because plus is on the, on one side of the equator, minus is on the other side of the equator. And even if you do the algebra, if you see that, I should flip it so it becomes, so the minus set 8 is 0 minus 1 by root 2.

Correct? If I do x on it, I am supposed to flip which essentially means I am going to apply the x on the minus state. This becomes what? 0 will become 1 minus 0 correct over root 2 which is actually equal to minus of 1 0 minus 1 root 2 which is equal to minus of the minus ket. So essentially just flips it on the. the sign changes. So, what has happened is that I have got a minus sign now.

So, where is the minus sign come? It has come on the target. Still now we are still okay, correct? Something has happened on the target. Nothing has happened on the control. We are consistent with the previous whatever I had written earlier. So, this minus sign is sitting on the controls one branch. Where is it sitting? sitting on the controls one branch, okay? Because a minus sign is exactly a Z, okay?

Okay, so the helper is the anchor and the kick travels back up the wire, okay? And so the key thing that is happening out here is that this particular effect, okay, makes your target, okay, makes your, so this is happening on the target. But because this is sitting on this place, the phase info actually comes from the target to the controller. This is known as my phase kickback. So is this clear? Because this is the most important thing about the CNOT gate.

So the target does not change the phase. There is a phase introduced into the target and that phase because there is this plus and minus floating around, correct? And the phase information actually gets encoded into the controls state. So this is known as my phase kickback. Because this is contrary to what the CNOT is supposed to do. CNOT essentially means that you're not going to change the condition of the controller.

You're not going to change the output of the control. And remember, you're not changing the state of the gate is not flipping. There's just a phase introduced out there. And remember, phase is really not measured. The relative phase is measurable, but global phase is not measurable. But we are going to use this phase to be able to tell me the answer to my balanced versus constant function.

OK.

## Kickback for the four oracles

So if you. So there are these my four oracles, correct? They are either telling me nothing, there is always zero, always one, copy and so these are my functions that I am going to, the oracle can implement these functions, correct? That's what we had started the discussion with. So, and what I'm going to now do is that I'm going to park the helper at minus, it is my helper is going to be initialized at minus state. I'm going to give a plus input.

Don't ask me how I'm going to give a plus input right away. But assuming that I can give a plus input, then the input wire, that means the control wire, with always zero will have nothing, with always one will have a sign on everything. With copy, it will have a Z-twist and flip it will have a Z-twist. So assign on everything means that we have global phase introduced, which essentially means that if you do just the maths, you'll see that if it's always zero, so if you start, you'll get a plus state out here. And for the balanced, you will get a negative state.

So for the constant, you will get plus state for the balanced, you will get a negative state. So what are we saying that with a single query, I will be able to tell whether my function is giving me a balanced, is an implementation of a balanced, is it a balanced function or a constant function? Yeah, okay. So that's idea, okay. So this is the first quantum algorithm, which is known as the Deutsch algorithm. Is this clear?

So as I said, we could be continuing with, helper is basically another extra qubit, X operator, There's no X operator, correct? There is a CNOT operator. So that is working on both of them together.

## Live demonstration using Quirk

So what I would like you to do now is to let us see this, some of this in simulation mode. So I posted a link. Let's go to that link. The link is visible or it's in your chat. So you should get a screen like this. So this is actually a very simple UI, which allows you to see the actions of your gates.

And you can build circuits on this. It's a composable framework. You can build circuits on this to actually see whatever we are doing in class. So for example, there are three lines that are there. So if you see the three lines in my diagram, so on this part of the thing. So what have I said? I have put two of them at ket zeros and one at ket one, correct?

And you are doing a measurement. So after measurement, you're seeing that there is one will be at one, which essentially means the lights are on. Therefore, you have a zero out there, one out there, and you have the offs representing the ket zero. And these are the positions of the qubits on. the Bloch sphere. So now if you want to bring in a say a suppose I want to invert this gate. So I have inverted this gate you see it becomes off.

So this is something that you can do. So if I bring in an H on this you will see it will go into a superposition state. So in a superposition state what does it mean that you measure a 0 or 1 with equal probability. So that is why 50 % is being shown out there and you see that it is sitting on the equator. You put another h out here, you will see that it again goes back to 0. You can change this to a 1, see that you're back to 1.

And we had x gate correct, hxx. So you see this is what we did, HZH. How did I add the third input, the third gate? Oh, that's easy. So you just take Take a Y, just bring it out here and put it there and then remove it. do it like that. That's how. So HZ should give you as a, so with zero it is giving you one.

Correct? And if I give a zero, if I give a one, I get a zero. So that means it is acting like a X gate. Okay. So now we want to do the CNOT thing. Correct? So let's assume that. So how do I do a CNOT? So this is the gate. I bring it here. they should be a CNOT. So you see with a control input of 0, I get a output 1.

If I change this to 1, I get a 0. So this is something that there many different gates that you can play around with and you can build. this is the first, it's a very intuitive one, which is useful to actually get a hang of how the gates operate and how the. So what did we say? We wanted to show the fact that if on my control I will have a plus and on my target I should have a minus. So you see measurement wise, they're still the same. Remember plus and minus are not distinguishable.

That's what we have. Probability wise, they are not distinguishable. But plus and minus can be distinguished if you have a H out there. So, I will put an h in either one of them. So, even then they are still not. So, I did get a phase somewhere correct. So, this particular example is, so if I put a single h, I can distinguish between the plus and minus states.

So, this then, this is a tool that you will use initially and there is the Qiskit framework which I will change the target output. We have to pass the input from the Oracle box. So the Oracle is actually the circuit gates. So the only thing is that when we say Oracle, when we do it from a CS or a maths perspective, this is known as a query model of complexity. We actually are given a box, we don't know about its implementation, we can just send it inputs and observe the outputs and from that we are trying to infer the behavior of that function. That's exactly what machine learning today is doing.

You are training, what do you mean by training a network? You're trying to estimate what the relationship is between the input and the output function. And you give it a lot number of data points to be able to correctly estimate the function. So here what are we saying? We are also estimating the function, correct? We're giving him different sorts of inputs to actually tell me whether the function is balanced or constant.

Okay, let's get back to my slides. there is this phase kickback that is happening. Your phase information is getting into the control. So that's the key thing that you have to remember from this discussion that if I have a CNOT, the target does not change, the control changes with the phase and there's a phase information which comes into the sync for certain sets of inputs. I've done it with plus and minus, there are other inputs on which you can also do it. Why do I do this business? that now that there is a difference and between these two lines I can actually use this phase information to be able to figure out what my function is.

## Deutsch’s circuit: preparing, querying, and measuring

And that's what your Deutsch circuit will do. The circuit which actually gives me the answer in a single query. So I take my helper bit which is initialized at zero. I put a x gate out there and do two Hadamard pass it through this oracle trying to figure out what that oracle is doing. And then I have another oracle, another H at the end, just like what I did earlier. And then I do a measurement.

Okay. So I spread the input to, so the input can be either zero or one, correct? But because the moment I use a Hadamard, I've actually put it into a plus or a minus state. Okay. So, so that's one thing, but the helper, I again use a Hadamard to actually also bring in the superposition state. Okay. So you do one query and then you decode.

If the input is zero, it's a constant. If the input is one, it is balanced. So we using this box, the Oracle box, only once. You're querying it only once. So that's the key thing.

## Constant and balanced cases, step by step

So if you do a step-by-step thing and the starting this thing, you have a zero. Just look at the input qubit because remember that becomes our control. So you start with this thing, look at the circuit, zero followed by H followed by a oracle and then another H. So zero H brings it to the plus state, apply the oracle and then you apply another H. If it is zero, you get a zero. So if it's a constant box, correct?

Remember it is always going to return a zero. That's our definition of a constant. does not change anything. So, and then if you apply another h, it brings it back to 0. So, I am trying to figure out what that box is. So, then you look at a balanced box. Balanced box should be returning a different quantity. So, I start again with 0, I have the helper bit.

Now, there is the oracle, the oracle will change the plus to a minus. Because remember, this is how we implemented the oracle.

We have these four oracle implementations. ok ok if it is a balanced thing it will where is it ok if it's balanced so then it will actually throw it it will change it's the plus will become a minus ok so the plus will become a minus so that's basically what you're doing so with the constant nothing happens with the balanced you get a minus so the plus has gone to the minus side because of the oracle and now you do a h you will now point it south correct because you have a minus so minus becomes a face and so you read a 1 and again you read it with 100 percent so that means if it is balanced you do it in one query if so one query settles the question because you either get a 0 or a 1 if you get a 0 you know that your function is balanced if you get a 1 you know your function is Well, if you get a zero, you know your function is constant.

If you get a one, you know your function is balanced. So this is the first algorithm which actually shows that you can do something in, you can get a speed up using a quantum algorithm. So this is basically the thing. The oracle secretly decides whether z sits between the two Hadamards and the answer comes out with Z. The helper wire is just helping you perform the exclusive or computation. So you can do these things in Quirk.

So you can probably do it in Quirk later.

## Interference as paths and arrows

So if you see what is actually happening from conceptually. okay, theoretically if I were to analyze what is exactly happening in this entire story. Okay, so you started with zero, okay, and then you applied an H, so the once you apply the H you actually went into zero and one, both of those you're in a superposition state, okay, and then at every state you had a fork, correct, okay, and then you applied another H, okay, the zero 0 goes to 0 and 0 can also come to 1, 1 can go to 0 and 1 to come to 1. So, actually had this sort of a path for the information flowing through the qubits.

So, two routes end at 0 and one at 1. So, every row carries an end. So, this is our convention. So if you have constructive interference, your path will become longer. If you have destructive interference, your path will become shorter. So now look at the constant box. So this would be for in general. Now let us bring the oracle in. Correct? Oracle is sitting between these two edges.

So now if you bring in the oracle box, so on these three paths with zeros, there's nothing happening on the one part you bring in the phase information and hence the destructively this thing. So, the routes to 1 cancel, the routes to 0 reinforce. So, plus and this plus and this minus would actually cancel out and these two would add up. So, this is the key intuition that you take. So, this is the path, I have not brought in my controlled-NOT as of now, I have not brought in the oracle. So, if I bring in the oracle, the oracle must sit somewhere here before the edge.

So, what is the function of the oracle? The oracle does something like this. On the zeros, it does not do anything, on the pluses it brings in the phase information. So if it brings in the, and where does it bring in the phase information? Remember we said it brings it onto the one line, the place where there's a one. So, so therefore it actually takes it to a zero out there.

Similarly for the balanced box, you will see that these two lines get flipped so that you are, the ones are, sorry, sorry. this and this get cancelling. So this and this get cancelled out. So therefore this goes out, whereas this and this are reinforced.

## Engineered cancellation and the quantum advantage

So the speed up that we get is an engineered cancellation. So how did we get this speed up? We have superposition. You have So you have a qubit, you have superposition, you have parallelism, okay, and you are actually able to do interference. The interference is coming because of quote unquote the entanglement. Okay. So all of those together give you the advantage. So there is parallelism, there is superposition, there is entanglement, but you have to engineer your solution so that you can construct use that you can use constructive interference to move your result towards one of the qubits.

As you see one towards one of the possibility because when you're going to do a measurement you should get it with absolute certainty. Okay so this is what we are trying. So the quantum algorithm arranges its route so that the wrong answers cancel out. Okay before you do the measurement. Remember after measurement you no longer have the quantum system. So till you have the quantum system, do things so that you can cancel out the wrong answers.

That's the key. You'll see that for all the quantum algorithms that we describe, this is the key thing that I should be able to use interference to move my solution towards the right answer. How do I do that? I cancel out the wrong answers. In this particular case, I had four paths. Two I used to bring, two are for the right answer, two are for the wrong answer.

Two of the wrong answer I try and use interference. I do something so that they are off of the opposite phases. And two, do such a thing so that they are in the right phase so that they add up. So this is what quantum algorithms are. I have to maximize the probability of success. That is my goal. How do I do it? I will use interference.

How do I do interference? On what do I do interference? I do interference on the different paths that my qubits can take. And how do I do that? I try and use the entangling gates in between and other gates. So this spread, the H opens up many routes. So if you have three qubits for example, three qubits means that two to the power three routes are possible.

For a single qubits I had two routes, correct? Now I have eight routes, correct? So I will do something so that my result will be amplified in four routes or they will constructively interfere in four and destructively interfere in two so that at the end of the day when I'm measuring I will actually get certain results. So, oracle is there, the oracle evaluates the function and h does the interference for you.

## Deutsch–Jozsa: extending to n bits

And then you can do the same analysis or the same sort of reasoning for n qubits. So, similarly here, so we did it, we saw with one qubit, the control if I actually do a CNOT between the control between the two qubits the phase information goes to the control. So now what I can do is that I can do it for all the other bits also or the other qubits also.

So I do the same thing I have the H for that's the spreader for all the input qubits and then for each of them I actually have the phase information in the control bit and hence you will see that if the function is balanced magically all the numbers or all the interferences towards all the paths which go towards 1 will cancel out. All the paths which go towards 0 will. So that means the output will be all zeros for a balanced function and the output will be all ones for a sorry, the output will be 0 for the constant function and the output will be 1 for a balanced function.

Do it qubit by qubit, you will see that it works out. Okay, as you remember the qubits are entangled to the last. So it's like each of these guys will have a connection here. This will have a connection here. This will have a connection here. So you can treat each of them separately, product systems and all that. When you do the algebra, you'll see that it works out.

Okay. So as I said, you'll have two to the power end routes instead of two for each constant box. The all zero scale is the same information. They all add up. For a balanced box half of them are flipped and they cancel completely. So the algebra we will do in the third lecture.

## Query complexity and practical context

Okay, so if you look at what is the advantage so if you have Classical this thing an algorithm with the 10 bits Okay, you have need 513 queries. That means 1024 by 2 by plus 1 Quantum you can within 1 if you have 100 qubits for 100 100 bit number you can still do it in one. So clearly you can, that's where the speed up of quantum machines is.

## Discussion: applications, verification, and limits

Now the question is, is this a useful algorithm? Is this used anywhere or will it be ever used? That's not very clear. That's not interesting for a mathematics or computer science perspective. It is basically the foundation for saying that, okay, there is one algorithm at least or one set of algorithms which can be accelerated. Okay, and this is a polynomial time algorithm to a linear time algorithm to constant time algorithm.

That's a huge result if you really look at it from a computer science complexity perspective. Okay, and this is what happened in 85 onwards. 85 and then 85, 86 and then 95 when Shor came about, they showed that you can take an exponential algorithm and bring it down to a linear. Okay, so this is something which is fundamental. This phase kickback is the key thing that you take back from this. That's the hardest concept that you need to initially internalize because I will use this phase kickback.

Amit is also going to use this phase kickback business almost like we do addition subtraction. Okay, for quantum that is the most important thing. This face back is back thing. So I tried to do without algebra. Most books only do it with algebra. I want you to actually, I'll give you those links. Those links are there in slides. So we can actually build the circuit for you.

You can build the circuits and then you can see where the movements of the control is on the Bloch sphere. That is what you should do. What is the query? We don't just get the constant and formula. No, we don't get what the function is. In either case, we don't get. Because as I told you, we are not interested in knowing what the function is.

I don't know what the, so, okay, what do you, I don't know whether it is flipping. What you are saying is that you can actually say whether the, if it is constant, whether the constant is zero or one. But, If it is a flip or copy, you don't know, correct? So I don't have, oh, you might know, but I'm not interested in that. don't, I am not interested in the, in whether the, what that function is. I'm just interested in knowing the, whether it is balanced or construct. So the Oracle is still a circuit.

You have to make that circuit. So that's what I did this four circuits for you. So we have a CNOT and. These are the four oracles, correct? One place I did keep the four oracles. So these are the four oracles or circuits, correct? So you have to build the circuits, otherwise how will you... So one of the things is that in this particular case, these circuits are very simple, but in real life for many algorithms, if you do just call oracle, oracle can be very complex.

Now 2 plus 4 is not working, not going to work. See, this is for quantum algorithms. So for example, can I do word on a quantum machine? No, you cannot. Can you do PowerPoint on a quantum machine? As of now, no. Can you do word on a GPU? No, correct? So the quantum computer by itself is not, it's going to be always as an accelerator.

Certain algorithms you can actually get a speed up. Not all algorithms can be speed up. No, that is also wrong. I've given you constant. You can say this is one probability, one you get an answer. the many places you get an answer is probability one. So, and you don't reduce any possibilities. You actually look through all possibilities. The quantum machine is evaluating all possibilities.

You are steering your vector towards the solution and the machine is always giving you a concrete outcome. That outcome can be 50 % 1, 50 % the same. So, there's always an outcome. Correct? and your model of computation is probabilistic. So, we can implement universal gates, you can CNOT plus X is actually, CNOT is actually a universal gate. So, if you can implement a universal gate in principle, you can do all possible computations, correct?

But so, in that sense, 2 plus 4 is also possible, but you wouldn't do 2 plus 4 out there. So, why would you build a quantum machine to do something it'll probably be way slower than any other machine, any classical machine. So optimization problems are problems that people are trying to solve using quantum machines. So what are the optimization problems? So for example, if you are trying to solve a set of linear equations, correct? So you can actually use a quantum machine to do that.

Things like solving differential equations in the quantum setting. quantum mechanics equations of quantum mechanics you want to simulate in quantum mechanics you do that on a quantum machine say the many body problem then people are trying to use it in chemistry so that is useful in chemistry also pharmacy pharmacy it is useful things which have low input this thing is number of inputs is limited is doable today on quantum machines Yeah, large search problems on what? The input is what? It's not very... That is a problem, correct? Large search problems, say for example, if you're looking for a solution in, say, for the... for protein, correct?

Then it's okay, but if you're at searching for a string in a human genome, I am not so sure. So one important question out here is that if something... If we say a quantum machine is capable of solving a problem, so this particular slide, correct? So for 100 qubits, it will take another part 29 seconds or some queries, correct? Which essentially is 20 trillion years on a classical machine. So can I guarantee myself that the solution that the quantum machine gives me in one query, is it correct?

Why do you think, why should I trust a quantum machine? That's a very big So, a solution that a quantum machine gives me, do you think, how do know it is correct? So, there must be a quick way of verifying it. So, it like if I can factor a number, that is one of the things that someone is going to teach you about, correct the factorization problem. Now, if you give him a 1000 digit number, the claim might be that in some time from now, 5 years from now, 7 years from now, A quantum machine definitely can break it but or factor it but a classical machine will not be able to do it.

But once that number has been factored, how do you know that the factors are correct? There is a polynomial time to do that because there's a fast method to figure out, the verification. So you can actually multiply those numbers out and see if it matches. So that's the problem where verification is easy. Now, if you are looking for a proverbial needle in a haystack, correct? And the condition might be the needle may not be also there.

So if that is a condition, then it tells me that there is a needle. How do I know that the needle exists? So that's his analysis is correct. But I'm looking for a certain set of proteins which are going to. that's not very clear as to how you're going to verify quantum algorithms. It's a very large, big area in reasonable amount of time. Ideal case of quantum computing for this thing is probably more classification.

Probably. Okay, that's number one. Number two, I would like to limit it to say anomaly detection or something like this. That's where I think people have made maximum progress. Nothing. There are things in quantum machine learning that can be done, can be applied. That's probably what Amit is going to talk about sometime later. But from an application perspective, think fraud detection or anomaly detection is what is likely to give better performance or a return on investment.

## Qiskit and the Jupyter Notebook demonstration

OK, so let me get back to the application skits. OK, so there is one other thing that I wanted to finish today that is this skits. I just wanted to do a quick poll. Python is okay with all of you, correct? Because that I think must be. So mostly yes, correct? Just wait for some more time. So because all of your CapsuleM projects are going to be in Qiskit or in Python.

Okay. Qiskit essentially. Quirk is essentially for. doing things quick and dirty method. You cannot really run an algorithm, large algorithms. It's like drawing, correct? If you have done any hardware design or you've done this drag and drop sort of coding, correct? The Scrabble, for example, if you have done that, then you know that it doesn't scale. You cannot build anything large. So do anything large, we'll actually work with Qiskit, correct?

And one of these days we'll actually have a... So one of the things that you do Qiskit on will be something that I'll show you. So where you, it's here. So essentially you have to get Qiskit installed on your machine. I will give you steps, it's there in IBM's website. So you can use either Qiskit or PennyLane, both of them are good, but I tend to use Qiskit because it is the best in the thing.

There are other things that you can do, other simulators also that you can do. Let me show you my Qiskit. So, I suppose the screen is visible to you. Yeah, it is. Okay. So, this is a Python file or Jupyter notebook, which essentially tells you basically what is it that you need to initially do. These are the preamble code that must be there in all of your programs.

Okay. So, in most cases, we will only work do in the simulation framework because simulation is the right way to actually work on these machines because you're trying to learn, correct? And the IBM machine actually, that's the only, they are the only ones which actually have a quantum computer which is available on the web. So they give you a 10 minute window per month, I think, so to, which is a free window. So what you can do is that, Many of these experiments, of these, so for example, this Deutsch algorithm that I talked about or variance of it, you actually don't want to use up that 10 minutes. You just get your entire algorithm working out here.

And only sometimes you might want to access that machine because the simulators that they give you, the Aer simulator that they give you is actually very, very faithful. It is only when you try and do this noise and error correction, that's when you really need real noise values to come from a simulator. Or if you're trying to actually work on say 20 qubits and 20 qubits simulating on your machine might be actually very slow and you want to see the speed up. So for example, on a classical simulator, one, so even this Deutsch algorithm, I'm saying that 10 qubits will take 513 queries on a classical machine.

But if you are running it on the simulator, you will see that the time it takes to answer that one simulator query itself might be more than what a classical machine might take. So that's where you might want to go into an actual quantum machine and get that answer to see that you really get fast answers. So we will have some exercise which will allow you to tell you basically how to do it from the Qiskit framework. But for most exercises, in fact, all capstone, et cetera, you will actually use the simulator.

## Practical labs and simulations

So for that clearly you have to use these functions. So this is basically just the import line which essentially tells you to do that. My iPad, do I actually go from this control enter. So then execute this line. So you see it prints the version and then the Hadamard gate should put it into superposition correct. So, if it's putting into superposition then how do what do you do?

So, you bring in the quantum circuit and you are going to simulate it using a state vector simulation. So, we are going to do the matrix you are going to do matrix vector multiplications that's essentially state vector it does not have noise in it. To bring in noise we use different models, but for now all your experiments you will using the state vector implementation. So if you want to do the state vector implementation, then you import state vector and you are using a single qubit and you're a Hadamard on that. So the draw function actually allows you to draw the circuit. So it draws a circuit and then you want to do the simulation.

For the simulation, you actually ask him to do simulation or state vector simulation of your Qc. Qc is remember the circuit this has just a single qubit so you should be able to and then you ask him to show it on the Bloch sphere. So it shows you on the Bloch sphere so 0 has come to the remember the plus sign this thing so on the x-direction on the equator. So this is something that we saw in the Quirk environment. the Quirk environment it was very small and you were not writing a program it was composable but here you can write it in the form of a program.

So and then you want to calculate the probabilities remember that's what we are interested in at some point when we do some algorithms we will see that the probability on Q0 measurement measuring on in the computational basis 0, mean ket 0 is one correct you want to see that or so okay so no quantum machine usage 10 minutes is free for more than 10 minutes is very expensive don't even try okay so it is 96 dollars per second and 96 rupees per second okay or 96 dollars per second one of one of those numbers i also don't use it okay so you see the probabilities are given like this okay so you see they are mostly uh close to one okay so we wanted to see the we did this Bell state the plus state which is the maximally entangled state.

So, what did I say you have to have a h on one qubit and a c naught after that. So, is the there a h and the c naught and then you want to draw the amplitudes correct. So, you will see that the amplitudes are equal on all four axis. So, the real and the imaginary in this and then with the simulator you want to simulate. Most of that was done using maths. Now if you want to do the simulation and you want to plot histograms etc.

So this particular sim equal to AerSimulator, is the place, this is the only line you change if you want to connect to a backend. So how much if you This is all possible on a laptop. No GPUs, no laptop. This works on a laptop. Currently I'm running this on... I've created this on a server because I will probably expose this as a server to you.

It's just that I've done a reverse proxy and some of these modules is not coming up through the reverse proxy. That's why I have not given it. Otherwise, we'll give you access to this... because the labs I've created are in this. format where I give you a file and on that file you go from one block to the next block only after you have answered the question correctly. So it's more like a self test for you. Okay, so now you see the two probabilities have come. So you have run the experiment for a thousand times.

I think so. You have run it for 1024 times and how many times have you got a zero and how many times have you got a one? Yes, every line would be available for you. So this is will be created for all the hundred people or whatever number of people that are there in the lab. will create that or Scalair will create that and we'll give it to you. Or we will give you the the Jupyter Labs. You can run it on your own laptop.

OK, so this is basically what I wanted to show you today. OK, so so for example, the This is something the practice lab that we will give you is something like this. So, for example, this particular I want to, we created the phi plus state. If I want to create the phi minus state, what will you do? So, these lines, the solution will not be there. It'll just have your code here.

So, you'll have to put in these lines to get this circuit. So, for example, I think I've solved the whole paper. the interesting, the important thing is that if you, once you solve this, only then the next blocks becomes enabled. So that's how I have planned it. So we'll try to give it to you on an IT daily server, but it also depends on whether I can make the reverse proxy work through our network guys. But otherwise you can do it on your own laptop. You don't even need a server class machine.

Okay, anything else that you would like? Let me see if I finished everything. So what you can today try is that once you get these lecture notes, you can try the Deutsch thing and then run 100 cents and you'll see that your answers are. So this is the important reason why you have to do it in Qiskit because on the Quirk, you can't actually run it for a hundred times, thousand times, correct? So here you want to run it for a thousand times to see that. Okay, so

## Three takeaways and closing questions

The three takeaways for today are that the function must be whatever quantum algorithm that we implement using Qiskit or any other programming environment must be a reversible function. That's the key thing. So for Deutsch’s algorithm, the helper, we keep the helper and implement the CNOT out there. Okay. The kickback, the helper is at this thing at the ket minus. So the answer is available as a phase in the control.

And then you have another H, which turns this twist into a readout. The wrong answers cancel. So in one sentence, you must take away from this lecture. The first two lectures of quantum computing is that it is not about trying every option at once. It is about making the wrong options cancel before you do the measurement. The first part is when you say trying every option at once means that you're doing a measurement of the ones.

That's not what quantum algorithm is. Quantum algorithm is that you perform something so that the wrong answers cancel out. So this is something that is a key takeaway that I would like you to go back from this class. So tomorrow, I think Amit will do a little bit maths because the linear algebra part must be clean. next Saturday I will actually do this entire thing more formally. that and I do one more couple of more of these algorithms so that we have the foundations in place. So what is the measurement of a qubit? Yes, it's a projection of one of the vectors, projection of a qubit, one of the lines on one of the computational base.

You can actually mathematically you can do it on any of the orthonormal basis. But if you're looking at a real measurement, then it is on one of the computational basis. Can we use VS code? It's your wish. I think it's all about writing Python, correct? Python, if you are comfortable on VS code, well and good. I don't have an issue. Any other questions?

Qiskit labs, you can practice on your own laptop. You don't need anything. What level of Python? You should know Python. That's because that's the amount of Python I know you don't really see the difference between Python and C is that C you really have to practice a lot. Python you get a lot of help from the world. One more question which was sent to me.

Is there any graded assignment to be completed for this week? Yeah. So that's why I finished at two o'clock today. I told you that it was going to be the second part is something that is the first real introduction to quantum because in the sense that you are actually doing this phase kickback business, correct? It's completely non-intuitive. Okay, I have said first that there's no change in the control, and then I'm saying that phase information is going to go to control.

There's obviously something wrong out there, correct? So there's nothing wrong because that phase information, remember, is something that I'm really not interested in because phased is not measurable unless I use some other gate, etc. But I can use that phase information to... actually perform this interference. Measurement is a non unitary operator. So hence once done, once measured you cannot change things. No, no graded assignment this week.

You might have something from omits this thing but it will still not be graded, it be practiced. I don't think we'll have anything later. No, phase is measurable only when you add with something else, correct? It is not measurable other on the wise correct anything on the equator on the y-axis x-axis is pleasant yes so you have multiple control inputs example correct multiple qubits all of them I have a it was like this correct so you have three lines and this is my ancillar okay or helper so I would have things like similar to this I have H here H here, H here. So this was my quote unquote Oracle, correct? And then I would have H, H and H.

So each of them, the phase information goes here. Each of these phase information goes here, phase information goes here, and the paths constructively or destructively interfere. We will do that. The cascade thing, let us do a little more of the algorithms first. because there's nothing much except for these. I would like you to first actually do a little bit on the work, this thing. Qiskit, let us wait a little more till we do a couple of more algorithms so that you can then go and do the, because quantum algorithms are six or seven lines of code, not more than that.

Okay, so the intuition, et cetera, be developed that first with small circuits so that you're able to think. particularly get familiar with the Bloch sphere. Basically how things move around in the Bloch sphere. So in that case, there are any more questions, otherwise we can close. Thanks, guys. Hope we see you next week. Bye bye. Thank you, professor. Have a nice day.

