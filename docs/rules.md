# Rules

> These are the rules used in the variation of Euchre implemented in **euchre-cli**.

## Setup

Euchre uses a non standard deck of 24 playing cards. It is composed of the Nine,
Ten, Jack, Queen, King, and Ace of each suit.

The first dealer is chosen randomly by turning a card from the deck for each player
until a black jack appears. For each subsequent hand, the player to the dealer's
left becomes the new dealer.

To start each hand, five cards are dealt to each player and the top card
of the remaining deck is turned face up.

## Calling Trump

After a hand is dealt, players must choose what the trump suit will be for that hand.
The suit of the face up card is the candidate trump suit.

Starting with the player to the dealer's left, and proceeding clockwise, each player
may elect to "pass", meaning they do not want the candidate to become trump, or they
may call "pick up", meaning the candidate suit becomes trump and the calling round
ends. The dealer then adds the face up card to their hand and discards a card to
the deck. Trick play may begin.

In the event that all players "passed" on the candidate suit, there is another calling
round. The face up card is turned over and added back to the deck. Then, starting
with the player to the dealer's left, each player may again elect to "pass", meaning
they do not want to call the trump suit. Or they may call any suit they have in their
hand to be trump (except the suit passed on in the previous round) and the calling
round ends. Trick play may begin.

> If all players once again have "passed" in the second calling round, the dealer
redeals the hand and the first calling round starts over.

## Card Weights

Cards of the trump suit are weighted higher than all others, but within the trump
suit the Jack (known as the Right Bower) is weighted highest. In addition, the Jack
belonging to the other suit of the same color as the trump suit (known as the Left
Bower) is considered the second best trump card. In fact, it is treated as if it
were the trump suit.

**For example**: If trump were Spades, the trump cards would be weighted in the
following order:

  1. Jack of Spades (Right Bower)
  2. Jack of Clubs (Left Bower)
  3. Ace of Spades
  4. King of Spades
  5. Queen of Spades
  6. Ten of Spades
  7. Nine of Spades

All other cards are weighted from high to low (Ace to Nine respectively), with
trump always beating the lead suit, and the lead suit always beating the others.

> Note: It is perfectly legal to play a trump card as the lead.

## Tricks

The player to the left of the dealer starts the first trick and they may lead with
a card of any suit - this suit will be known as the lead suit. Play then proceeds
clockwise with each player playing a card of the lead suit if they have one, otherwise
they may play any card, including trump. Once each player has played a card, the
player who played the card with the highest weight takes the trick and leads the
next trick.

Tricks are played until all players are out of cards.

## Scoring

The team that takes the majority of the tricks in a hand (3 or more) wins that hand
and is awarded points. The number of points awarded is as follows:

| The winning team...                   | Points    |
| :---                                  | :---      |
| called trump and took 3 or 4 tricks   | +1        |
| called trump and took all 5 tricks    | +2        |
| did not call trump                    | +2        |

## Winning

The first team to 10 points has won the game!

<div style="text-align: right">Last updated: {docsify-updated}</div>
