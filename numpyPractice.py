{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-a4d87639838a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0ma\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marray\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\numpy.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     45\u001b[0m   {\n\u001b[0;32m     46\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 47\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     48\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     49\u001b[0m    \u001b[1;34m\"outputs\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=np.array([1,2,3,4,5])\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5,)\n",
      "1\n",
      "1 2\n",
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "print(a.shape)\n",
    "print(a.ndim)\n",
    "print(a[0],a[1])\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "b=np.array([1,2],[2,3.],[4,5+1j])\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0.]\n",
      " [0. 0.]]\n",
      "[[1. 1.]\n",
      " [1. 1.]\n",
      " [1. 1.]]\n",
      "[[7 7]\n",
      " [7 7]]\n",
      "[[1. 0.]\n",
      " [0. 1.]]\n",
      "[[0.17417914 0.45227868]\n",
      " [0.64209587 0.59559658]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=np.zeros((2,2))\n",
    "b=np.ones((3,2))\n",
    "c=np.full((2,2),7)\n",
    "d=np.eye(2)\n",
    "e=np.random.random((2,2))\n",
    "print(a)\n",
    "print(b)\n",
    "print(c)\n",
    "print(d)\n",
    "print(e)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2.+0.j, 3.+0.j, 4.+0.j, 5.+0.j, 6.+0.j, 7.+0.j, 8.+0.j, 9.+0.j])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(10)\n",
    "np.arange(2,3,0.1)\n",
    "np.arange(2,10,dtype=complex)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1. , 1.6, 2.2, 2.8, 3.4, 4. ])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linspace(1,4,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[[0, 0, 0, 0],\n",
       "         [0, 0, 0, 0]],\n",
       "\n",
       "        [[1, 1, 1, 1],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[2, 2, 2, 2],\n",
       "         [2, 2, 2, 2]],\n",
       "\n",
       "        [[3, 3, 3, 3],\n",
       "         [3, 3, 3, 3]],\n",
       "\n",
       "        [[4, 4, 4, 4],\n",
       "         [4, 4, 4, 4]],\n",
       "\n",
       "        [[5, 5, 5, 5],\n",
       "         [5, 5, 5, 5]],\n",
       "\n",
       "        [[6, 6, 6, 6],\n",
       "         [6, 6, 6, 6]],\n",
       "\n",
       "        [[7, 7, 7, 7],\n",
       "         [7, 7, 7, 7]]],\n",
       "\n",
       "\n",
       "       [[[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]],\n",
       "\n",
       "        [[0, 0, 0, 0],\n",
       "         [1, 1, 1, 1]]],\n",
       "\n",
       "\n",
       "       [[[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]],\n",
       "\n",
       "        [[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]],\n",
       "\n",
       "        [[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]],\n",
       "\n",
       "        [[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]],\n",
       "\n",
       "        [[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]],\n",
       "\n",
       "        [[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]],\n",
       "\n",
       "        [[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]],\n",
       "\n",
       "        [[0, 1, 2, 3],\n",
       "         [0, 1, 2, 3]]]])"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.indices((8,2,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3  4]\n",
      " [ 5  6  7  8]\n",
      " [ 9 10 11 12]]\n",
      "(3, 4)\n",
      "[[5 6 7 8]]\n"
     ]
    }
   ],
   "source": [
    "a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])\n",
    "print(a)\n",
    "print(a.shape)\n",
    "print(a[1:2,:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "77\n"
     ]
    }
   ],
   "source": [
    "a[0,0]=77\n",
    "print(a[0,0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2]\n",
      " [ 6]\n",
      " [10]]\n"
     ]
    }
   ],
   "source": [
    "print(a[:,1:2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[77  6  9]\n"
     ]
    }
   ],
   "source": [
    "print(a[[0,1,2],[0,1,0]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 4]\n",
      " [3 3 3]\n",
      " [3 3 3]\n",
      " [4 4 4]]\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "index 4 is out of bounds for axis 1 with size 3",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-96-7e2ddb54835f>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mb\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marray\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m4\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: index 4 is out of bounds for axis 1 with size 3"
     ]
    }
   ],
   "source": [
    "a=np.array([[1,2,4],[3,3,3],[3,3,3],[4,4,4]])\n",
    "print(a)\n",
    "b=np.array([4,5,3,4])\n",
    "print(a[np.arange(4),b])\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [ 7  8  9]\n",
      " [10 11 12]]\n",
      "[0 0 0 1]\n",
      "[ 1  4  7 11]\n",
      "[[ 2  2  3]\n",
      " [ 5  5  6]\n",
      " [ 8  8  9]\n",
      " [10 12 12]]\n"
     ]
    }
   ],
   "source": [
    "a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])\n",
    "print(a)\n",
    "b=np.array([0,0,0,1])\n",
    "print(b)\n",
    "print(a[np.arange(4), b])\n",
    "a[np.arange(4),b]+=1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 3  5  5  6  8  8  9 10 12 12]\n"
     ]
    }
   ],
   "source": [
    "bool_idx=(a>2)\n",
    "print(a[bool_idx])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "int32\n",
      "float64\n",
      "int32\n",
      "[1 2]\n"
     ]
    }
   ],
   "source": [
    "x=np.array([1,2])\n",
    "print(x.dtype)\n",
    "y=np.array([1.,2])\n",
    "print(x.dtype)\n",
    "x=np.array([1,2],dtype=int)\n",
    "print(x.dtype)\n",
    "print(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2. 4.]\n",
      "[2. 4.]\n",
      "[0. 0.]\n",
      "[0. 0.]\n",
      "[1. 4.]\n",
      "[1. 4.]\n",
      "[1. 1.]\n",
      "[1. 1.]\n"
     ]
    }
   ],
   "source": [
    "y=np.array([1.,2])\n",
    "print(x+y)\n",
    "print(np.add(x,y))\n",
    "print(x-y)\n",
    "print(np.subtract(x,y))\n",
    "print(x*y)\n",
    "print(np.multiply(x,y))\n",
    "print(x/y)\n",
    "print(np.divide(x,y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[21 24]\n",
      " [26 31]]\n"
     ]
    }
   ],
   "source": [
    "v=np.array([[1,2,4],[2,3,4]])\n",
    "w=np.array([[1,2],[4,5],[3,3]]) #row of 1 matrix should be equal to column of other matrix\n",
    "print(v.dot(w))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "[4 6]\n",
      "[3 7]\n",
      "[[1 3]\n",
      " [2 4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "x=np.array([[1,2],[3,4]])\n",
    "print(np.sum(x))\n",
    "print(np.sum(x,axis=0))\n",
    "print(np.sum(x,axis=1))\n",
    "print(x.T.T.T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 2  4  3  6]\n",
      " [ 5  7  6  5]\n",
      " [ 2  8  7 11]]\n",
      "[[ 2  4  3  6]\n",
      " [ 5  7  6  5]\n",
      " [ 2  8  7 11]]\n"
     ]
    }
   ],
   "source": [
    "x=np.array([[1,2,3,3],[4,5,6,2],[1,6,7,8]])\n",
    "v=np.array([1,2,0,3])\n",
    "y=np.empty_like(x)\n",
    "print(x+v)\n",
    "for i in range(3):\n",
    "    y[i,:]=x[i,:]+v\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3]\n",
      "[[1]\n",
      " [2]\n",
      " [3]]\n",
      "[1 2 3]\n",
      "[[1]\n",
      " [2]\n",
      " [3]]\n"
     ]
    }
   ],
   "source": [
    "v=np.array([1,2,3])\n",
    "print(v)\n",
    "print(np.reshape(v,(3,1)))\n",
    "print(v)\n",
    "v=np.reshape(v,(3,1))\n",
    "print(v)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "#img=cv2.imread('test_image.jpg')    #changed image format to jpg\n",
    "#cv2.namedWindow('img',cv2.WINDOW_NORMAL)\n",
    "#cv2.waitKey(0)\n",
    "#cv2.imshow('cv2.WINDOW_NORMAL',img)\n",
    "#cv2.destoryAllWindows()\n",
    "\n",
    "image=cv2.imread('C:\\\\Users\\\\Aparajita\\\\.spyder-py3\\\\image1.jpg')\n",
    "\n",
    "cv2.namedWindow('image',cv2.WINDOW_NORMAL)\n",
    "\n",
    "cv2.imshow(\"my\",image)\n",
    "\n",
    "cv2.waitKey()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
