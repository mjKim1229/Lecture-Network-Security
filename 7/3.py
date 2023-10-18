import boto3

def compare_faces(image_path1, image_path2):
    client = boto3.client('rekognition')
    
    with open(image_path1, 'rb') as image_file1, open(image_path2, 'rb') as image_file2:
        image_data1 = image_file1.read()
        image_data2 = image_file2.read()
    
    response = client.compare_faces(
        SourceImage={'Bytes': image_data1},
        TargetImage={'Bytes': image_data2},
    )
    
    # Get the similarity score
    similarity_score = response['FaceMatches'][0]['Similarity']
    
    return similarity_score

def main():
    image_path1 = '3-1.jpg' 
    image_path2 = '3-2.jpg'  

    similarity_score = compare_faces(image_path1, image_path2)
    
    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()

