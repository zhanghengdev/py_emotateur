# Introduction d'Algorithme

## Détection des points d'interets des visages

Détection des points d'intérêts sur la visage de référence et la visage d’utilisateur avec la bibliothèque openpose. La sortie de cette partie est une matrice de numpy pour chaque visage sous la forme(70*3):

|   | la coordonnee de x  |  la coordonnee de y  | la probabilité de chaque point |
|---|---|---|---|
| point 0 |   |   |   |
| point 1 |   |   |   |
| point 2 |   |   |   |
|  ... |   |   |   |
| point 69  |   |   |   |

La répartition des points est comme ça:

![](keypoints_face.png) 

On va nommer la matrice des points d'interets du visage référence `face_key_points_1` et d’utilisateur `face_key_points_2`.

## Vérification de détection

Si la moyenne de ces probabilités du visage d'utilisateur est inférieur à 0.5, on va quiter la fonction.
Sinon on met les probabiliés 1.

```python
# check if most part of the face is detected
score = np.mean(face_key_points_2[:, 2])
if score < 0.5:
    return 0
face_key_points_1[:, 2] = 1
face_key_points_2[:, 2] = 1
```

## Alignement du visage

Maintenant on regroupe ces 70 points à 2 groupes:

1. groupe 1: `location_indexes`
```python
location_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                27, 28, 29, 30]
```
1. groupe 2: `signature_indexes`
```python
signature_indexes = [17, 18, 19, 20, 21,                                # left eye brow
                22, 23, 24, 25, 26,                             # right eye brow
                36, 37, 38, 39, 40, 41,                         # left eye
                42, 43, 44, 45, 46, 47,                         # right eye
                48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, # outside mouth
                60, 61, 62, 63, 64, 65, 66, 67,                 # inside mouth
                68, 69]                                         # pupil
```

On assume que la translation de visage est une **translation affine**, alors on va calculer la matrice de translation `T` avec l'ensemble de groupe 1 `location_indexes`:

```python
# alignement
location_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                                27, 28, 29, 30]
I = np.transpose(face_key_points_2[location_indexes, :])
I_p = np.transpose(face_key_points_1[location_indexes, :])
T = np.dot(I_p, pinv(I))
```

Après effectuer la transformation `T` aux points d’utilisateur `face_key_points_2`, **les deux visages auront la même position, échellee et angle.**

## Comparasion

### Matrice de signature

Pour chaque visage, on va construire une matrice de signature avec** les vecteurs de la point de référence (30: pointe du nez) à tous les points de groupe `signature_indexes`.**
**Attention: avant de calculer la matrice de signature d'utilisateur, faire l'alignement du visage avant! (Ça veut dire effectuer la translation T)**

```python
# vectors
signature_indexes = [17, 18, 19, 20, 21,                                # left eye brow
                22, 23, 24, 25, 26,                             # right eye brow
                36, 37, 38, 39, 40, 41,                         # left eye
                42, 43, 44, 45, 46, 47,                         # right eye
                48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, # outside mouth
                60, 61, 62, 63, 64, 65, 66, 67,                 # inside mouth
                68, 69]                                         # pupil
center_index = 30
# vectors_1
vectors_1 = face_key_points_1[signature_indexes, :2] - face_key_points_1[center_index, :2]
# vectors_2
face_key_points_2_signature_aligned = np.transpose(np.dot(T, np.transpose(face_key_points_2[signature_indexes, :])))
face_key_points_2_center_aligned = np.transpose(np.dot(T, np.transpose(face_key_points_2[center_index, :])))
vectors_2 = face_key_points_2_signature_aligned[:,:2]-face_key_points_2_center_aligned[:2]
```

### Calcul de la distance entre ces 2 matrices de signature

On peut utiliser la distance d'euclidean ou la distance cosine.

```python
# Euclidean distance
euclidean_distance = 0
for i in range(len(signature_indexes)):
    euclidean_distance += distance.euclidean(vectors_1[i, :], vectors_2[i, :])
```

```python
# cos distance
cos_distance = 0
for i in range(len(signature_indexes)):
    cos_distance += distance.cosine(vectors_1[i, :], vectors_2[i, :])
```

Après pluseurs essais, la premiere marche un peu mieux.

### Utiliser la somme de la distance carré

Pour négliger l'impact de bruits et la difference  d‘apparence des visages, on va effectuer une fonction:
$$y=x^2$$

```python
# squared Euclidean distance
squared_euclidean_distance = 0
for i in range(len(signature_indexes)):
    squared_euclidean_distance += (distance.euclidean(vectors_1[i, :], vectors_2[i, :])/10)**2
```

**Remarque**, peut-etre la fonction soft l1 est mieux:
$$y=x^2 \ \ si\  x \leq thresh$$
$$y=|x| \ \ si \ x > thresh$$

### Filtage gaussienne

Utiliser une filtre gaussienne à rendre la résultat plus stable:

```python
# Gauss filter
gauss_filter = [7/74, 26/74, 41/74]
# squared Euclidean distance
squared_euclidean_distance = 0
for i in range(len(signature_indexes)):
    squared_euclidean_distance += (distance.euclidean(vectors_1[i, :], vectors_2[i, :])/10)**2
self.last_distance_2 = self.last_distance_1
self.last_distance_1 = self.last_distance_0
self.last_distance_0 = squared_euclidean_distance
squared_euclidean_distance = np.dot(gauss_filter, [self.last_distance_2, self.last_distance_1, self.last_distance_0])
```