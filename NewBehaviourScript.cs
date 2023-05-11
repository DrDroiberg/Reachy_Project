using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    
    void Start()
    {
        WebCamTexture webcamTexture = new WebCamTexture();
	  Debug.Log(webcamTexture.deviceName);

	  Renderer renderer = GetComponent<Renderer>();
	  renderer.material.mainTexture = webcamTexture;
	  webcamTexture.Play();
    }

   

}
