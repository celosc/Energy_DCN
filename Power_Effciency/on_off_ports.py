#Liga uma porta do switch.

QTDE_PORTAS_SWITCH = 48 
    
#Tipos dos switches
#ACESSO = 0;
#AGREGACAO = 1
#NUCLEO = 2
    
#Estados das portas dos switches. */
DESLIGADA = 0
FAST_ETH = 1
GIGA_ETH = 2
GIGA_10_ETH = 3
 
#Consumo por tipo de porta dos switches. */
consumoFastEth = 0.3
consumoGigaEth = 0.5
consumo10GigaEth = 5.0;

     
    # A largura de banda agregada do switch 
#(soma das larguras de banda de todas as portas de downlink ligadas).

bwAgregada = None

def PowerSwitch(idSwitch, tipo, qtdePortas):
    
    Id(idSwitch)
    Tipo(tipo)
    QtdePortas(qtdePortas)
    QtdePortasAtivas(qtdePortas)
    EstadoPorta([qtdePortas])
    ConsumoInicioFrame(0.0)
    Ligado=True

    
    '''
     * Cria um objeto PowerSwitch.
     *
     * @param idSwitch o id do switch
     * @param tipo o tipo do switch
     * @param qtdePortas a quantidade total de portas do switch
     * @param qtdePortasUplink a quantidade de portas de uplink do switch 
     '''

      

#Liga o switch.

def ligaSwitch():
        #Liga o switch
    Ligado=True
        
       
    print ("Switch de %s #%d foi ligado.", type , IdSw)

#Desliga o switch.

def desligaSwitch():
        
#Desliga o switch
    Ligado=False
        
        #Atualiza o consumo
     ConsumoAtual=0  

    print ("Switch de %s #%d foi desligado.", type , IdSw)

  
    #
#Liga uma porta do switch.

def ligaPorta(numPorta):
        
     #Incrementa a quantidade de portas ativas do switch
     QtdePortasAtivas(QtdePortasAtivas() += 1)
        
    #Determina o consumo e a largura de banda da porta
     consumoPorta = retornaConsumoPorta(estadoPorta[numPorta])
     bwPorta = retornaBwPorta(estadoPorta[numPorta])
        
    #Atualiza o consumo atual do switch
    ConsumoAtual(getConsumoAtual() + consumoPorta);
        
     #Atualiza a largura de banda agregada (se a porta não é de uplink)
        if(!ePortaDeUplink(numPorta)){
            BwAgregada(getBwAgregada() + bwPorta)
            
            
            print ("Porta #%d do switch de %s #%d foi ligada.", numPorta, Tipo, Id)

    
    #
     #Desliga uma porta do switch.

def desligaPorta(numPorta):
     #Determina o consumo e a largura de banda da porta antes de desligá-la
     consumoPorta = retornaConsumoPorta(estadoPorta[numPorta])
     bwPorta = retornaBwPorta(estadoPorta[numPorta])
        
#Desliga a porta
    estadoPorta[numPorta] = DESLIGADA
        
    #Decrementa a quantidade de portas ativas do switch
    QtdePortasAtivas(QtdePortasAtivas() -= 1)
        
     #Atualiza o consumo atual do switch
     ConsumoAtual(getConsumoAtual() - consumoPorta);
        
        #Atualiza a largura de banda agregada (se a porta não é de uplink)
        if(!ePortaDeUplink(numPorta)){
            BwAgregada(BwAgregada() - bwPorta); 

                
        
        if(ePortaDeUplink(numPorta)) 
            Log.formatLine(
                    "Porta #%d (uplink) do switch de %s #%d foi desligada.",
                    numPorta,
                    tipoParaString(getTipo()),
                    getId());
        else
            Log.formatLine(
                    "Porta #%d do switch de %s #%d foi desligada.",
                    numPorta,
                    tipoParaString(getTipo()),
                    getId());

    #
#Aumenta a velocidade de uma porta do switch.

def aumentaVelocidadePorta(numPorta)
#Armazena o consumo e a largura de banda da porta antes de aumentar a velocidade 
     consumoAnteriorPorta = retornaConsumoPorta(estadoPorta[numPorta])
     bwAnteriorPorta = retornaBwPorta(estadoPorta[numPorta]);
        
     #Aumenta a velocidade da porta
        estadoPorta[numPorta]++;
        
        #Se a porta não é de uplink
        if(!ePortaDeUplink(numPorta)){
           #Armazena a largura de banda após aumentar a velocidade
           int bwPorta = retornaBwPorta(estadoPorta[numPorta]);
           
           #Atualiza a largura de banda agregada
           setBwAgregada(getBwAgregada() + (bwPorta-bwAnteriorPorta));

        #Armazena o consumo da porta após diminuir a velocidade
        double consumoPorta = retornaConsumoPorta(estadoPorta[numPorta]);
        
     #Atualiza o consumo atual do switch                
    ConsumoAtual(ConsumoAtual() + (consumoPorta-consumoAnteriorPorta));

    
    
    #
#Reduz a velocidade de uma porta do switch.

def reduzVelocidadePorta(numPorta){
     #Armazena o consumo e a largura de banda da porta antes de diminuir a velocidade 
     consumoAnteriorPorta = retornaConsumoPorta(estadoPorta[numPorta]);
     bwAnteriorPorta = retornaBwPorta(estadoPorta[numPorta]);
        
     #Reduz a velocidade da porta
     estadoPorta[numPorta]--;
        
     #Se a porta não é de uplink
        if(!ePortaDeUplink(numPorta)){
           #Armazena a largura de banda após diminuir a velocidade
           int bwPorta = retornaBwPorta(estadoPorta[numPorta]);
           
           #Atualiza a largura de banda agregada
           BwAgregada(getBwAgregada() - (bwAnteriorPorta-bwPorta));
           
           
        
        #Armazena o consumo da porta após diminuir a velocidade
        consumoPorta = retornaConsumoPorta(estadoPorta[numPorta]);
        
        #Atualiza o consumo atual do switch                
        ConsumoAtual(getConsumoAtual() - (consumoAnteriorPorta-consumoPorta));

       
    

     #Calcula o consumo atual do switch.

#calculaConsumoAtual(){
        
    #Percorre todas as portas do switch e adiciona ao seu consumo atual o consumo de cada uma
        for(i=0; i<QtdePortas(); i++)
            switch(estadoPorta[i])
                case DESLIGADA: 
                    break;
                case FAST_ETH: 
                    ConsumoAtual(ConsumoAtual() + ConsumoFastEth()); 
                    break;
                case GIGA_ETH:
                    ConsumoAtual(ConsumoAtual() + ConsumoGigaEth());
                    break;
                case GIGA_10_ETH:
                    ConsumoAtual(ConsumoAtual() + Consumo10GigaEth());
                    break;
                case GIGA_40_ETH:
                    ConsumoAtual(ConsumoAtual() + Consumo40GigaEth());
                    break;
                case GIGA_100_ETH:
                    ConsumoAtual(ConsumoAtual() + Consumo100GigaEth());
                    break;

    
    #
#Calcula o consumo do switch durante um frame da simulação.

def calculaEnergiaConsumidaFrame(duracaoFrame)
    consumoFrame;
        
    consumoFrame = ((ConsumoInicioFrame() + ConsumoAtual()) / 2) * duracaoFrame;
        
    ConsumoInicioFrame(getConsumoAtual());
        
        return consumoFrame;

    
     
    #
#Calcula a largura de banda agregada do switch.
     #Não considera as portas de uplink.

def alculaBwAgregada()
     BwAgregada(0);
        
        for(i=0; i<QtdePortas()-QtdePortasUplink(); i++)
            switch(estadoPorta[i])
                case DESLIGADA: 
                    break;
                case FAST_ETH: 
                    BwAgregada(BwAgregada() + 100);
                    break;
                case GIGA_ETH:
                    setBwAgregada(BwAgregada() + 1000);
                    break;
                case GIGA_10_ETH:
                    setBwAgregada(BwAgregada() + 10000);
                    break;
                case GIGA_40_ETH:
                    BwAgregada(BwAgregada() + 40000); 
                    break;
                case GIGA_100_ETH:
                    BwAgregada(BwAgregada() + 100000);
                    break;

    
    #
#Retorna o consumo atual de um tipo de porta.

def retornaConsumoPorta(estadoPorta){
        
        switch(estadoPorta){
                case DESLIGADA: 
                    return 0.0;
                case FAST_ETH: 
                    return ConsumoFastEth();
                case GIGA_ETH:
                    return ConsumoGigaEth(); 
                case GIGA_10_ETH:
                    return Consumo10GigaEth(); 
                case GIGA_40_ETH:
                    return Consumo40GigaEth();
                case GIGA_100_ETH:
                    return Consumo100GigaEth(); 
                default:
                    return 0.0; 

    
    #
#Retorna a largura de banda de uma porta.

def retornaBwPorta(estadoPorta){
       
        switch(estadoPorta){
                case DESLIGADA: 
                    return 0;
                case FAST_ETH: 
                    return 100; 
                case GIGA_ETH:
                    return 1000;
                case GIGA_10_ETH:
                    return 10000;
                case GIGA_40_ETH:
                    return 40000;
                case GIGA_100_ETH:
                    return 100000;
                default:
                    return 0;


#Retorna a string correspondente ao estado de uma porta.

def estadoPortaParaString(numPorta)

        
        switch(estadoPorta[numPorta])
            case DESLIGADA: 
                    estadoString = "Desligada";
                    break;
            case FAST_ETH: 
                    estadoString = "Fast Ethernet";
                    break;
            case GIGA_ETH:
                    estadoString = "Gigabit Ethernet";
                    break;
            case GIGA_10_ETH:
                    estadoString = "10 Gigabit Ethernet";
                    break;
            case GIGA_40_ETH:
                    estadoString = "40 Gigabit Ethernet";
                    break;
            case GIGA_100_ETH:
                    estadoString = "100 Gigabit Ethernet";
                    break;
            default:
                    break;

        
        return estadoString;

    
    #
#Retorna a string correspondente ao tipo do switch.
'''
def tipoParaString(tipo){
        String tipoString = null;
        
        switch(tipo){
            case ACESSO: 
                    tipoString = "acesso";
                    break;
            case AGREGACAO: 
                    tipoString = "agregação";
                    break;
            case NUCLEO:
                    tipoString = "núcleo";
                    break;
            default:
                    break;
        }
        
        return tipoString;
    }

    
    #
#Retorna os atributos do switch.

    @Override
    public String toString() {
        return "PowerSwitch{" + "id=" + getId() + ", tipo=" + getTipo() + 
                ", qtdePortas=" + getQtdePortas() + ", qtdePortasUplink=" + getQtdePortasUplink() + 
                ", qtdePortasAtivas=" + getQtdePortasAtivas() + ", consumoAtual=" + getConsumoAtual() +
                ", consumoInicioFrame=" + getConsumoInicioFrame() + ", ligado=" + getLigado() +
                ", bwAgregada=" + getBwAgregada() + ", estadoPortas=" + Arrays.toString(getEstadoPorta()) + '}';
    }
'''
