import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

"""
Example for MLP

TF-IDF con logistic regression

"""

# ===========================
# 1. Example Dataset
# ===========================



texts = [
    "Che film fantastico!",
    "Orribile, non lo guarderò mai più",
    "Mi è piaciuto molto",
    "Non mi è piaciuto per niente",
    "Una bella esperienza",
    "Brutto e lento"
]

labels = [1, 0, 1, 0, 1, 0]  # 1 = positivo, 0 = negativo

# ===========================
# 2. TF-IDF Vectorization
# ===========================

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts).toarray()
y = np.array(labels)

# ===========================
# 3. Train/Test Split
# ===========================

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ===========================
# 4. Model Building
# ===========================

model = Sequential()
model.add(Dense(16, input_dim=X.shape[1], activation='relu'))  # Hidden layer
model.add(Dense(1, activation='sigmoid'))  # Output binario

model.compile(optimizer=Adam(learning_rate=0.01),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# ===========================
# 5. Training
# ===========================

print("\n📚 Inizio training...\n")
model.fit(X_train, y_train, epochs=10, batch_size=2, verbose=1)

# ===========================
# 6. Evaluation
# ===========================

print("\n🧪 Valutazione sul test set:\n")
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\n✅ Accuracy: {accuracy*100:.2f}%")

# ===========================
# 7. New Phrase Prediction
# ===========================

new_text = ["Il film è stato davvero bello"]
new_vec = vectorizer.transform(new_text).toarray()
prediction = model.predict(new_vec)

print(f"\n🧾 Predizione su nuova frase: \"{new_text[0]}\"")
print(f"📊 Probabilità sentiment positivo: {prediction[0][0]:.2f}")

print("")
print(X)