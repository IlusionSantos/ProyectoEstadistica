
# coding: utf-8

# # <center>Distribuciones Bivariables</center>

# ## Definición 
# Sea $X_1$ y $X_2$ dos variables aleatorias discretas. La distribución de probabilidad conjunta para $X_1$ y $X_2$ está dada por:<br>
# $$p(x_1,\,x_2)=P(X_1(r)=x_1;\, X_2(r)=x_2)$$
# <br>
# Definida sobre los reales $X_1$ y $X_2$.
# 
# ### Teorema
# Si $X_1$ y $X_2$ son variables aleatorias discretas con función de probabilidad conjunta $p(x_1,\, x_2)=f(x_1,\, x_2)$.
# <ol>
# <li value=1>$p(x_1,\, x_2)=f(x_1,\, x_2)\ge 0, \,\, \forall x_1,\, x_2$</li>
# <li>$\sum_{x_1}\sum_{x_2}p(x_1,\, x_2)=1$</li>
# </ol>

# ### Ejemplo
# Para el lanzamiento de dos dados $P(2\le X_1\le 3,\, 1\le X_2\le2)=?$<br>
# $X_1\rightarrow$ el número de puntos en la cara superior del primer dado<br>
# $X_2\rightarrow$ el número de puntos en la cara superior del segundo dado
# <br>
# Recordando el ejemplo de el lanzamiento de dos dados, cada uno tiene probabilidad de $\displaystyle\frac{1}{36}$.
# <br>
# <br>
# 
# $$\begin{eqnarray} P(2\le X_1\le3,\, 1\le X_2\le2) & = & p(2,1)+p(2,2) + p(3,1) + p(3,2)
# \\ & = & \displaystyle\frac{1}{36}+\displaystyle\frac{1}{36} +\displaystyle\frac{1}{36} + \displaystyle\frac{1}{36}
# \\ & = & \displaystyle\frac{4}{36} = \displaystyle\frac{1}{9}
# \end{eqnarray}$$
# 

# ## Distribuciones Bivariables Continuas
# ### Definición
# Para la pareja de variables $X_1$ y $X_2$, la función de distribución conjunta $F(a,b)$, está dada por:
# $$F(a,b)=P(X_1\le a;\, X_2\le b)$$
# ### Definición
# Sean $S_1$ y $X_2$ variables aleatorias continuas con función de distribución conjunta $F(a,b)$. Si existe una función no negativa $f(a,b)$ tal que:
# $$F(a,b)=\displaystyle\int_{-\infty}^a \displaystyle\int_{-\infty}^bf(x_1,\, x_2)\, dx_2dx_1$$
# 
# ### Propiedades
# Sean $X_1$ y $X_2$ variables aleatorias continuas con función de distribución conjunta $F(a,b)$.
# <ol>
# <li value=1>$F(-\infty, -\infty)=F(-\infty,x_2)=F(x_1,-\infty)=0$</li>
# <li>$F(\infty,\infty)=1$</li>
# <li>Si $a\ge x_1$ y $b\ge x_2$ entonces:</li>
# </ol>
# $$F(a,b)-F(x_1,b)-F(a,x_2)+F(x_1,x_2)\ge 0$$

# ## Distribución de Probabilidad Marginal
# ### Definición
# Sean $X_1$ y $X_2$ variables aleatorias conjuntas discretas, con función de probabilidad conjunta $p(x_1,x_2)$. Entonces las funciones de probabilidad marginales de $X_1$ y $X_2$ respectivamente están dadas por:
# $$p_1(x_1)=\sum_{x_2}p(x_1,x_2) \hspace{2cm} p_2(x_2)=\sum_{x_1}p(x_1,x_2)$$
# 
# <br>
# En el caso de las variables continuas en forma similar tenemos:
# $$f_1(x_1)=\displaystyle\int_{-\infty}^{\infty}f(x_1,x_2)\,dx_2 \hspace{2cm} 
# f_2(x_2)=\displaystyle\int_{-\infty}^{\infty}f(x_1,x_2)\,dx_1$$
# <br><br>
# ## Distribución de probabilidad Condicional Discreta
# ### Definición
# Sean $X_1$ y $X_2$ variables aleatorias conjuntas discretas, con función de probabilidad conjunta $p(x_1,x_2)$ y funciones de probabilidad marginales $p_1(x_1)$ y $p_2(x_2)$ respectivamente, entonces la función de densidad de probabilidad condicional discreta de $X_1$ dada por $X_2$ es:<br><br>
# $$p_1(x_1\, |\, x_2)= P(X_1=x_1 \, | \, X_2=x_2)= \displaystyle\frac{P(X_1=x_1 \land X_2=x_2)}{P(X_2=x_2)}$$
# <br>
# Donde el numerador es la distribución conjunta y el denominador es la distribución marginal.
# <br>
# De igual forma se puede escribir:
# $$p_1(x_2\, |\, x_1)= \displaystyle\frac{P(X_1=x_1 \land X_2=x_2)}{P(X_1=x_1)}$$
# 
# ## Distribución de probabilidad Condicional Continua
# ### Definición
# Sean $X_1$ y $X_2$ variables aleatorias conjuntas continuas, con función de probabilidad conjunta $f(x_1,x_2)$ entonces la función de densidad de probabilidad condicional continua de $X_1$ dada por $X_2=x_2$ es:<br><br>
# $$F(X_1 \, | \, X_2)=P(X_1\le x_1 \, | \, X_2=x_2)$$<br><br>
# Y de igual forma:
# $$F(X_2 \, | \, X_1)=P(X_2\le x_2 \, | \, X_1=x_2)$$
# <br><br>
# ### Definición
# Sean $X_1$ y $X_2$ variables aleatorias conjuntas continuas, con función de probabilidad conjunta $f(x_1,x_2)$ y densidad marginales $f_1(x_1)$ y $f_2(x_2)$  entonces la función de densidad de probabilidad condicional continua de $X_1$ dada por $X_2=x_2$ es:<br><br>
# $$f(x_1\, | \, x_2) = \left \{ \begin{matrix} \displaystyle\frac{f(x_1,x_2)}{f_2(x_2)} & f_2(x_2)>0
# \\ 0 & \mbox{e.o.p.}
# \end{matrix}\right.$$
# <br><br>
# Y la condicional de $X_2$ dada por $X_1=x_1$
# $$f(x_2\, | \, x_1) = \left \{ \begin{matrix} \displaystyle\frac{f(x_1,x_2)}{f_1(x_1)} & f_1(x_1)>0
# \\ 0 & \mbox{e.o.p.}
# \end{matrix}\right.$$

# ### Ejemplo
# De un grupo de tres republicanos, dos demócratas y un independiente, debe seleccionarse al azar un comité de dos personas. Sea $X_1$ el número de republicanos y $X_2$ el número de demócratas en el comité. Encontrar la distribución de probabilidad conjunta de $X_1$, $X_2$ y luego la distribución marginal de $X_1$.
# $X_1 \rightarrow$ número de republicanos $=0,1,2$ de los $3$ posibles
# $X_2 \rightarrow$ número de demócratas $=0,1,2$ de los $2$ posibles
# $2-X_1-X_2 \rightarrow$ número de independientes $=0,1$ del único posible
# <br><br>
# 
# La función de densidad conjunta se define de la siguiente forma:<br>
# $$p(x_1 \, | \, x_2)=P(X_1=x_1 \, | \, X_2=x_2)=
# \displaystyle\frac{\displaystyle\binom{3}{X_1}\displaystyle\binom{2}{X_2}\displaystyle\binom{1}{2-X_1-X_2}}{\displaystyle\binom{6}{2}}$$
# <br>
# Comenzando con $x_1=0$ y $x_2=0$ nos damos cuenta que no es posible ya que solamente hay una persona independiente, así que al menos debe de haber un republicano o un demócrata. Por lo que:<br>
# $p(0,0)=0 \leftarrow$ por definición del problema.<br>
# $p(1,0)=\displaystyle\frac{\displaystyle\binom{3}{1}\displaystyle\binom{2}{0}\displaystyle\binom{1}{1}}{\displaystyle\binom{6}{2}}=\displaystyle\frac{3}{15}$<br>
# $p(0,01)=\displaystyle\frac{\displaystyle\binom{3}{0}\displaystyle\binom{2}{1}\displaystyle\binom{1}{1}}{\displaystyle\binom{6}{2}}=\displaystyle\frac{2}{15}$<br>
# $p(1,1)=\displaystyle\frac{\displaystyle\binom{3}{1}\displaystyle\binom{2}{1}\displaystyle\binom{1}{0}}{\displaystyle\binom{6}{2}}=\displaystyle\frac{6}{15}$<br><br>
# Nos damos cuenta que para los siguientes no está definido ya que solo pueden haber $2$ personas en el comité:<br>
# $p(2,1)=p(1,2)=p(2,2)=0\rightarrow$ por definición del problema
# 
# <table class="egt">
#     <tr>
#         <td rowspan="2", WIDTH=50><b><center>$x_2$</center></b></td>
#         <td colspan="3", WIDTH=200><b><center>$x_1$</center></b></td>
#         <td rowspan="2"><b><center>Total</center></b></td>
#     </tr>
#     <tr>
#         <td><b><center>$0$</center></b></td>
#         <td><b><center>$1$</center></b></td>
#         <td><b><center>$2$</center></b></td>
#     </tr>
#     <tr>
#         <td><b><center>$0$</center></b></td>
#         <td><center>$0$</center></td>
#         <td><center>$\displaystyle\frac{3}{15}$</center></td>
#         <td><center>$\displaystyle\frac{3}{15}$</center></td>
#         <td><center>$\displaystyle\frac{6}{15}$</center></td>
#     </tr>
#     <tr>
#         <td><b><center>$1$</center></b></td>
#         <td><center>$\displaystyle\frac{2}{15}$</center></td>
#         <td><center>$\displaystyle\frac{6}{15}$</center></td>
#         <td><center>$0$</center></td>
#         <td><center>$\displaystyle\frac{8}{15}$</center></td>
#     </tr>
#     <tr>
#         <td><b><center>$2$</center></b></td>
#         <td><center>$\displaystyle\frac{1}{15}$</center></td>
#         <td><center>$0$</center></td>
#         <td><center>$0$</center></td>
#         <td><center>$\displaystyle\frac{1}{15}$</center></td>
#     </tr>
#     <tr>
#         <td><b><center>Total</center></b></td>
#         <td><center>$\displaystyle\frac{3}{15}$</center></td>
#         <td><center>$\displaystyle\frac{9}{15}$</center></td>
#         <td><center>$\displaystyle\frac{3}{15}$</center></td>
#         <td><center>$1$</center></td>
#     </tr>
# </table>
# 
# <br><br>
# Del lado derecho de la tabla se muestra en la columna del total la distribución marginal de $X_2$.<br>
# En la parte inferior de la tabla en la fila del Total se muestra la distribución marginal de $X_1$. Por lo que la función de distribución marginal de $X_1$ queda:
# <table class="egt">
#     <tr>
#         <td WIDTH=50><b><center>$x_1$</center></b></td>
#         <td WIDTH=50><b><center>$0$</center></b></td>
#         <td WIDTH=50><b><center>$1$</center></b></td>
#         <td WIDTH=50><b><center>$2$</center></b></td>
#     </tr>
#     <tr>
#         <td><center>$p(x_1)$</center></td>
#         <td><center>$\displaystyle\frac{3}{15}$</center></td>
#         <td><center>$\displaystyle\frac{9}{15}$</center></td>
#         <td><center>$\displaystyle\frac{3}{15}$</center></td>
#     </tr>
# </table>
# 
# 
# 
# 

# ## Valor Esperado de Bivariables
# El valor esperado de $X_1$ y $X_2$ se define como:<br><br>
# $$E[g(x_1,x_2)]=\sum_{x_1}\sum_{x_2}g(x_1,x_2)p(x_1,x_2)$$
# $$E[g(x_1,x_2)]=\displaystyle\int_{-\infty}^{\infty}\displaystyle\int_{-\infty}^{\infty}g(x_1,x_2)f(x_1,x_2)\,dx_1dx_2$$
# <br><br>
# El valor esperado de bivariables cumple con las siguientes propiedades:
# <ol>
# <li value=1>$E[cg(x_1,x_2)]=cE[g(x_1,x_2)]$</li>
# <li>$E[g_1(x_1,x_2)+...+g_k(x_1,x_2)]=E[g_1(x_1,x_2)]+...+E[g_k(x_1,x_2)]$</li>
# </ol>

# ## Covarianza de Bivariables
# La covarianza de $X_1$ y $X_2$ se define como el valor esperado de $(x_1-\mu_1)(x_2-\mu_2)$ y se denota como:
# $$cov(X_1,X_2)=E[(x_1-\mu_1)(x_2-\mu_2)]$$
# con:
# $$\mu_1=E(X_1) \hspace{2cm} \mu_2=E(X_2)$$
# <br><br>El coeficiente de correlación se define entonces como:
# $$r=\displaystyle\frac{cov(X_1,X_2)}{\sigma_1\sigma_2}$$
# <br><br>
# Donde $r$ toma valores entre $1 \le r\le 1$ y mira la relación entre la variable $X_1$ y la variable $X_2$. Mientras más cercano sea $|r|$ a $1$ más relación lineal existe entre las variables $X_1$ y $X_2$.<br><br>
# 
# ## Variables Aleatorias Independientes
# Sean $X_1$ y $X_2$ variables aleatorias discretas (continuas) con función de densidad de probabilidad conjunta $p(x_1,x_2)$, para las variables discretas y $f(x_1,x_2)$ para las variables continuas; y funciones de densidad marginal $p_1(x_1)$ y $p_2(x_2)$, para las variables discretas; y $f_1(x_1)$ y $f_2(x_2)$, para las variables continuas respectivamente, entonces $X_1$ y $X_2$ son independientes si:<br><br>
# $$p(x_1,x_2)=p_1(x_1)\cdot p_2(x_2) \hspace{1cm} \forall x_1,x_2...$$
# <br>
# $$f(x_1,x_2)=f_1(x_1)\cdot f_2(x_2) \hspace{1cm} \forall x_1,x_2...$$
# 
# Si $X_1$ y $X_2$ con variables aleatorias conjuntas con función de densidad conjunta $f(x_1,x_2)$, entonces:
# $$cov(X_1,X_2)=E[(x_1-\mu_1)(x_2-\mu_2)]=E(X_1,X_2)-E(X_1)E(X_2)$$
# <br><br>
# Si $X_1$ y $X_2$ con variables aleatorias independientes, entonces:
# $$cov(X_1,X_2)=0$$
# 

# ### Ejemplo
# Sean $X_1$ y $X_2$ las proporciones de tiempo, en un día de trabajo que dos empleados ocupan en hacer sus tareas asignadas respectivamente. El comportamiento de las frecuencias relativas conjuntas de $X_1$ y $X_2$ se representan en el modelo de la función de densidad:<br>
# 
# $$f(x_1,x_2) = \left \{ \begin{matrix} x_1+x_2 & 0\le x_1 \le 1\, 0\le x_2 \le 1 
# \\ 0 & \mbox{en otras partes}
# \end{matrix}\right.$$
# Encontrar:
# <ol>
# <li value=1>$P(x_1<\displaystyle\frac{1}{2},x_2>\displaystyle\frac{1}{4})$</li>
# <li>$P(x_1+x_2<1)$</li>
# </ol>

# Resolviendo el primer inciso:
# $$\begin{eqnarray} P \left ( x_1<\displaystyle\frac{1}{2},x_2>\displaystyle\frac{1}{4} \right ) & = & \displaystyle\int_{\frac{1}{4}}^{1}\displaystyle\int_{0}^{\frac{1}{2}}(x_1+x_2)\,dx_1dx_2
# \\ & = & \displaystyle\int_{\frac{1}{4}}^1 \left (\displaystyle\frac{1}{8}+\displaystyle\frac{x_2}{2} \right )\,dx_2
# \\ & = & \displaystyle\frac{21}{64}
# \end{eqnarray}$$
# <br><br>
# Resolviendo el segundo inciso:
# $$P(x_1+x_2 < 1)$$

# In[2]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[4]:

data = [1,0]
plt.figure()
plt.plot(data,'m-o',markersize=8)
plt.axis([-0.10, 2.0, -0.15, 2])

