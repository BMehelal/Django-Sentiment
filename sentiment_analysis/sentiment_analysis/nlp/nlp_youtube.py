from transformers import AutoTokenzier, AutoModelForSequenceClassification
from scipy.special import softmax
from sentiment_analysis.models import Comments


def nlp_youtube():
    # gets all the comments from the database
    id_with_content = list(Comments.objects.values_list('id', 'content'))

    # Load tokenizer and model
    
    # Tokenize the input
    inputs = tokenizer(content, return_tensors="tf",
                       padding=True, truncation=True)

    # Get model predictions
    outputs = model(inputs)

    # Get logits (raw scores) from the model
    logits = outputs.logits

    # Convert logits to predicted class (0 for negative, 1 for neutral, 2 for positive)
    predicted_classes = tf.argmax(logits, axis=1).numpy()

    # Print predicted classes for each comment
    for i, prediction in enumerate(predicted_classes):
        print(f"Comment {i + 1}: Predicted class = {prediction}")


nlp_youtube()
